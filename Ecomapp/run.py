from flask import Flask
from products import routes


app = Flask(__name__)
app.secret_key = 'secret'


if __name__ == '__main__':
    app.run()