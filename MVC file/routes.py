from flask import request, jsonify
from . import create_app
from . import services

app = create_app()


@app.route('/blog', methods=['POST'])
def create_post():
    data = request.get_json()
    post = services.create_post(data['title'], data['content'])
    return jsonify(post), 201


@app.route('/blog', methods=['GET'])
def get_all_posts():
    posts = services.get_all_posts()
    return jsonify(posts), 200


@app.route('/blog/<post_id>', methods=['GET'])
def get_post(post_id):
    post = services.get_post(post_id)
    if post:
        return jsonify(post), 200
    return jsonify({"message": "Post not found"}), 404


@app.route('/blog/<post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    post = services.update_post(post_id, data['title'], data['content'])
    if post:
        return jsonify(post), 200
    return jsonify({"message": "Post not found"}), 404


@app.route('/blog/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    services.delete_post(post_id)
    return jsonify({"message": "Post deleted"}), 200
