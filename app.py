# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Flask, render_template

from models      import db, MonthlyCustomers, MonthlySales, ProductSales
from api         import blueprint
from data_loader import data_importer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']        = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def index():
    return render_template("index.html") 

@app.cli.command("load-data")
def load_data():
    db.create_all()
    data_importer(db, MonthlyCustomers, 
                "data/monthly_customers.csv", 
                ["month_name", "customer_count"], [str, int])
    data_importer(db, MonthlySales, 
                "data/monthly_sales.csv", 
                ["month_name", "sale"], [str, int])
    data_importer(db, ProductSales, 
                "data/product_sales.csv", 
                ["product", "sale"], [str, int])

@app.before_first_request
def initialize_database(): 
    db.create_all() 

db.init_app(app)
    
app.register_blueprint(blueprint, url_prefix="/api")

