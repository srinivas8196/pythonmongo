from flask import Flask, jsonify, session, request
from pymongo import MongoClient

## set up mongo configuration
## setting up the connection
##set up the DB
## set up the collections /objects / models

dbclient = MongoClient("mongodb+srv://batch6:herovired@cluster0.aqifkg2.mongodb.net/")
db = dbclient["pythonshop"]
products_collection = db["pythonshop"]
order_collection = db["pyshoporders"]
cart_collection = db["pyshopcarts"]


app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# products = {
#     1: {'name': 'Product 1', 'price': 10.99, 'description': 'Description 1', 'image_url': 'image1.jpg'},
#     2: {'name': 'Product 2', 'price': 19.99, 'description': 'Description 2', 'image_url': 'image2.jpg'},
#     3: {'name': 'Product 3', 'price': 7.99, 'description': 'Description 3', 'image_url': 'image3.jpg'}
# }

cart = {}
orders = []


@app.route("/")
def index():
    return jsonify(message="Welcome to the e-commerce application!")


@app.route("/products", methods=["GET"])
def get_products():
    ##database query from MongoDB
    products = list(products_collection.find({}, {"_id": 0}))
    return jsonify(products)


# JSON data
# {
#   "name": "New Product",
#   "price": 24.99,
#   "description": "Description of the new product",
#   "image_url": "new_product.jpg"
# }


@app.route("/products", methods=["POST"])
def add_product():
    product = request.get_json()
    # product_id = len(products) + 1
    ## products[product_id] = product
    products_collection.insert_one(product)
    return jsonify(message=f"Product '{product['name']}' added successfully!")


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    if product_id in products_collection:
        product = request.get_json()
        products_collection.update_one({}, {"_id": 0}, set(product))
        # products[product_id] = product
        return jsonify(message=f"Product with ID '{product_id}' updated successfully!")
    else:
        return jsonify(error=f"Product with ID '{product_id}' does not exist!")


@app.route("/cart/add/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    product = products_collection.get(product_id)
    if product:
        if "cart" not in session:
            session["cart"] = {}
            if product_id not in session["cart"]:
                session["cart"][product_id] = product
                return jsonify(
                    message=f"Product '{product['name']}' added to cart successfully!"
                )
            else:
                return jsonify(
                    message=f"Product '{product['name']}' is already in the cart!"
                )
    else:
        return jsonify(error=f"Product with ID '{product_id}' does not exist!")


@app.route("/cart", methods=["GET"])
def view_cart():
    if "cart" in session:
        cart = session["cart"]
        total_price = sum(product["price"] for product in cart.values())
        return jsonify(cart=cart, total_price=total_price)
    else:
        return jsonify(message="Your cart is empty!")


@app.route("/cart", methods=["DELETE"])
def clear_cart():
    if "cart" in session:
        session.pop("cart")
        return jsonify(message="Cart cleared successfully!")
    else:
        return jsonify(message="Your cart is already empty!")


@app.route("/orders", methods=["POST"])
def place_order():
    if "cart" in session:
        cart = session.pop("cart")
        orders.append(cart)
        return jsonify(message="Order placed successfully! Your cart has been cleared.")
    else:
        return jsonify(message="Your cart is empty!")


@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders=orders)


@app.route("/orders/<int:order_index>", methods=["PUT"])
def update_order(order_index):
    if order_index >= 0 and order_index < len(orders):
        order = request.get_json()
        orders[order_index] = order
        return jsonify(
            message=f"Order with index '{order_index}' updated successfully!"
        )
    else:
        return jsonify(error=f"Order with index '{order_index}' does not exist!")


if __name__ == "__main__":
    app.run()
