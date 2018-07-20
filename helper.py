from pymongo import MongoClient

def add_item(name, desc, price, img):
    client = MongoClient()
    items = client.space.items
    items.insert_one({"name": name, "description": desc, "price": price, "image_url": img})
