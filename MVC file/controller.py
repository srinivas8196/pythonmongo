from .models import Blog, db, ObjectId


def create_post(title, content):
    post = {"title": title, "content": content}
    post_id = db.blog.insert_one(post).inserted_id
    return get_post(post_id)


def get_all_posts():
    posts = db.blog.find()
    return [Blog.to_json(post) for post in posts]


def get_post(post_id):
    post = db.blog.find_one({"_id": ObjectId(post_id)})
    if post:
        return Blog.to_json(post)


def update_post(post_id, title, content):
    db.blog.update_one({"_id": ObjectId(post_id)}, {
                       "$set": {"title": title, "content": content}})
    return get_post(post_id)


def delete_post(post_id):
    db.blog.delete_one({"_id": ObjectId(post_id)})
