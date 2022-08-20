from flask import Flask, request, Response
from database.db import initialize_db
from database.models import PropertyReviews, LandlordReviews, Property, Landlord

app = Flask(__name__)


app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/RateMyLandlord'
}

initialize_db(app)


@app.route('/properties')
def get_properties():
    properties = Property.objects().to_json()
    return Response(properties, mimetype="application/json", status=200)

@app.route('/landlords')
def get_landlords():
    landlords = Landlord.objects().to_json()
    return Response(landlords, mimetype="application/json", status=200)

@app.route('/properties', methods=['POST'])
def add_property():
    body = request.get_json()
    property = Property(**body).save()
    id = property.id
    return {'id': str(id)}, 200

@app.route('/movies/<id>', methods=['PUT'])
def update_property(id):
    body = request.get_json()
    Property.objects.get(id=id).update(**body)
    return '', 200

@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    Property.objects.get(id=id).delete()
    return '', 200

app.run()