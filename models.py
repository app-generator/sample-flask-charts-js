
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class MonthlyCustomers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month_name = db.Column(db.String(8), nullable=False, unique=True)
    customer_count = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.month_name : self.customer_count}"

class MonthlySales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month_name = db.Column(db.String(8), nullable=False, unique=True)
    sale = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.month_name : self.sale}"

class ProductSales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(50), nullable=False, unique=True)
    sale = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.product : self.sale}"