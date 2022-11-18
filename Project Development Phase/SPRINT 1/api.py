from flask import Flask
from dbConnect import connection
app = Flask(__name__)


@app.route("/")
def hello_world():
    connection()
    return "<p>Hello, World!</p>"
