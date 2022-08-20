from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from DbPost import CLIENT, DB

APIKEY = "vbmEkLeatM1hrMXBsRMJiyDOojk7HOPHRKM1oGYcBXBfK0d45nnSn71vFYuAkWwQ"

app = Flask(__name__)

app.config['MONGO_DBNAME'] = "RateMyLandlord"
app.config['MONGO_URI'] = "mongodb://localhost:27017/RateMyLandlord"

mongo = PyMongo(app)

@app.route('/properties', methods=['GET'])
def get_all_properties():
    property = mongo.db.properties

    output = []
       
    for i in property.find():
        output.append({"type": i['type'], "address": i['address'], "images": i['images'], "rooms": i['rooms'], "bathrooms": i['bathrooms'], "price": i['price'], "LandlordName": i['LandlordName'], "StarRating": i['StarRating'], "reviews": [{"title": i['title'], "body": i['body']}, {"title": i['title'], "body": i['body']}]})

    return jsonify({"result": output})