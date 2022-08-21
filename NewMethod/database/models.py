from .db import db


class PropertyReviews(db.EmbeddedDocument):
    Title = db.StringField(required=True)
    Body = db.StringField(required=True)


# LANDLORD PAGE COMMENT FORMAT Stars, Address, Title, Body

class Landlords(db.Document):
    meta = {"collection": "Landlords"}
    LandlordName = db.StringField(required=True)
    Stars = db.IntField(required=True, min_value=0, max_value=10)
    Address = db.StringField(required=True)
    Title = db.StringField(required=True)
    Body = db.StringField(required=True)


class Properties(db.Document):
    meta = {"collection": "Properties"}
    Category = db.StringField(required=True)
    Address = db.StringField(required=True)
    Campus = db.StringField(required=True)
    Images = db.ImageField(required=True, unique=True,
                           size=None, thumbnail_size=None)
    Rooms = db.IntField(required=True, min_value=0)
    Bathrooms = db.IntField(required=True, min_value=0)
    Price = db.IntField(required=True, min_value=0)
    LandlordName = db.StringField(required=True)
    StarRating = db.StringField(required=True, min_value=0, max_value=10)
    Reviews = db.EmbeddedDocumentField(PropertyReviews)
