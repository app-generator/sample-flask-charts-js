import os
import click
from flask import Flask, render_template
from requests import get

from api import blueprint


CHART_DATA_URL = "https://gist.githubusercontent.com/swapniljariwala/fe30b41b31a20488567b04786eb90e04/raw/733c61745323fac653b28e047119ab34c620fbb5/dataset.json"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.cli.command("load-data")
def load_data():
    try:
        os.makedirs("data")
    except FileExistsError:
        pass

    try:
        resp = get(CHART_DATA_URL)
        click.echo(click.style("Successfully fetched the data.", fg='green'))
    except:
        click.echo(click.style("Could not fetch the data", fg='red'))
        return

    data_path = os.path.join("data", "dataset.json")
    
    with open(data_path, "w") as fp:
        fp.write(resp.text)
        click.echo(click.style(f"Saved data to {data_path}.", fg='green'))

app.register_blueprint(blueprint, url_prefix="/api")

