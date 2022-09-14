print ("Hello all!!")

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello AIDI 1001</p>"