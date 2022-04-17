from flask import Flask, render_template
from api import blueprint

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


app.register_blueprint(blueprint, url_prefix="/api")