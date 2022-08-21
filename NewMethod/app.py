from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Properties, Landlords
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://admin:admin@cluster0.bk4dmsx.mongodb.net/RateMyLandlord'
}

initialize_db(app)


@app.route('/properties', methods=['GET'])
def get_properties():
    properties = Properties.objects().to_json()
    return Response(properties, mimetype="application/json", status=200)


@app.route('/landlords', methods=['GET'])
def get_landlords():
    landlords = Landlords.objects().to_json()
    return Response(landlords, mimetype="application/json", status=200)


@app.route('/properties', methods=['POST'])
def add_property():
    body = request.get_json()
    property = Properties(**body).save()
    id = property.id
    return {'id': str(id)}, 200


@app.route('/properties/<id>', methods=['PUT'])
def update_property(id):
    body = request.get_json()
    Properties.objects.get(id=id).update(**body)
    return '', 200


@app.route('/properties/<id>', methods=['DELETE'])
def delete_movie(id):
    Properties.objects.get(id=id).delete()
    return '', 200


app.run()
