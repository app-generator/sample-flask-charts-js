import json
from flask import Blueprint
from flask_restx import Api, Resource


blueprint = Blueprint('api', __name__)
api = Api(blueprint)

def read_data():
    with open("data/dataset.json") as fp:
        dataset = json.load(fp)
    return dataset

@api.route("/MonthlySales")
class MonthlySales(Resource):
    def get(self):
        dataset = read_data()
        return dataset['monthly_sales']

@api.route("/DailySales")
class DailySales(Resource):
    def get(self):
        dataset = read_data()
        return dataset['daily_sales']

@api.route("/SalesByCategory")
class SalesByCategory(Resource):
    def get(self):
        dataset = read_data()
        return dataset['sales_by_category']