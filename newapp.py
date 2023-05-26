from flask import Flask,jsonify,request,session
from pymongo import MongoClient

cart = []
orders = {}

app = Flask(__name__)
app.secret_key = 'secret'

dbclient = MongoClient('mongodb+srv://batch6:herovired@cluster0.aqifkg2.mongodb.net/')
db = dbclient['pythonshop']
product_collection = db['pythonshop']
order_collection = db ['pythoporders']
cart_collection = db['pyshopcart']

@app.route('/')
def index():
    return jsonify('Welcome to pyshop')

@app.route('/products',methods=['GET'])
def get_products():
    products = product_collection.find({},{'_id': 0})
    return jsonify(list(products))
    
@app.route('/products/<int:id>',methods=['GET'])
def get_product(id):
    product = product_collection.find_one({'id': id}, {'_id': 0})
    if product:
        return jsonify(product)
    return jsonify('Product not found')

@app.route('/addproduct', methods = ['POST'])
def add_product():
    product = request.get_json()
    product_collection.insert_one(product)
    return jsonify('Product added succesfully')

@app.route('/update/{_id}', methods = ['PUT'])
def update_product(product_id):
    product = product_collection.find_one({'_id': product_id})
    if product:
        product_collection.update_one({'_id': product_id}, {'$set': product})
        return jsonify('Product updated succesfully')
    return jsonify('Product not found')


@app.route('/addtocart',methods=['POST'])
def add_to_cart(product_id):
    product = product_collection.find_one({'_id': product_id})
    if product:
        cart.append(product)
        return jsonify('Product added to cart succesfully')
    return jsonify('Product not found')


    



# @app.route('/cart',methods=['GET'])
# def get_cart():
#     if cart_collection in session:
#         cart = session['cart']

#     return jsonify(cart)


# @app.route('/cart/<int:product_id>',methods=['DELETE'])
# def remove_from_cart(product_id):
#     product = product_collection.find_one({'_id': product_id})
#     if product:
#         cart.remove(product)







if __name__ == '__main__':
    app.run()