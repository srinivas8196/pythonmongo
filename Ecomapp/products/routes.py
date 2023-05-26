from flask import request, jsonify
from . import create_app
from . import controller

app = create_app()

@app.route("/",methods=['GET'])
def index():
    return jsonify("App is running")

@app.route("/products", methods=["GET"])
def get_products():
    products =controller.get_products()
    return jsonify(list(products))

