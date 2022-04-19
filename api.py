import json
from flask import Blueprint, request
from flask_restx import Api, Resource, fields
from models import  db, MonthlyCustomers, MonthlySales, ProductSales

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

customer_model = api.model("Monthly Customers", {
    "month_name": fields.String,
    "customer_count": fields.Integer
})

@api.route("/MonthlyCustomers")
class MonthlyCustomersAPI(Resource):
    
    @api.marshal_with(customer_model,  envelope='data')
    def get(self, **kwargs):
        """Monthly Customer Count
        Returns monthwise customer count
        """
        return MonthlyCustomers.query.all()


    @api.expect(customer_model, validate=True)
    def post(self, **kwargs):
        """Monthly Customer Count
        Creates an entry in DB of customer count for a month

        
        """
        data = request.get_json()
        row = MonthlyCustomers(**data)
        db.session.add(row)
        db.session.commit()
        return {"status": "success"}

sales_model = api.model("Monthly Sales", {
    "month_name": fields.String,
    "sale": fields.Integer
})

@api.route("/MonthlySales")
class MonthlySalesAPI(Resource):

    @api.marshal_with(sales_model,  envelope='data')
    def get(self, **kwargs):
        """Monthly Sales
        Returns monthwise sales
        """
        return MonthlySales.query.all()


    @api.expect(sales_model, validate=True)
    def post(self, **kwargs):
        """Monthly Sales
        Creates an entry in DB of a sale for a month
        """
        data = request.get_json()
        row = MonthlySales(**data)
        db.session.add(row)
        db.session.commit()
        return {"status": "success"}


product_model = api.model("Product Sales", {
    "product": fields.String,
    "sale": fields.Integer
})


@api.route("/ProductSales")
class SalesByCategoryAPI(Resource):
    @api.marshal_with(product_model,  envelope='data')
    def get(self, **kwargs):
        """Product  Sale
        Returns sale by product
        """
        return ProductSales.query.all()


    @api.expect(product_model, validate=True)
    def post(self, **kwargs):
        """Product  Sale
        Creates an entry in DB of sale for a product
        """
        data = request.get_json()
        row = ProductSales(**data)
        db.session.add(row)
        db.session.commit()
        return {"status": "success"}

