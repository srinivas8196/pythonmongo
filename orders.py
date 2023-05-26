from flask import Flask, jsonify, session,request
from pymongo import MongoClient

dbclient = MongoClient('mongodb+srv://batch6:herovired@cluster0.aqifkg2.mongodb.net/')
db = dbclient('pythonshop')
order_colection = db('pyshoporders')

app = Flask(__name__)

orders = []

@app.route('/')
def index():
    return jsonify('Welcome to Python shop')

# @app.route('orders')
# def get_orders():
