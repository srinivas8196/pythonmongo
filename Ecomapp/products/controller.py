from .models import db,product_collection
from flask import jsonify

def get_products():
  products = product_collection.find_one({},{"_id":0}) 
  return jsonify(list(products))