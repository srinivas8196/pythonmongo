from pymongo import MangoClient

dbclient = MangoClient("mongodb+srv://batch6:herovired@cluster0.aqifkg2.mongodb.net/")
db = dbclient("pythonshop")
order_collection = db("pyshoporders")
