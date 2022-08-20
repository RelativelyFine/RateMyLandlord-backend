from .db import db

#PROPERTIES FORMAT: type (apartment, condo, house - string), location (address - string), images, rooms(int), bathrooms(int), price(int), LandlordName(string), StarRating (1-10 int), reviews (address, title and body -strings)
#LANDLORD REVIEW FORMAT: address, title, body - strings

#LANDLORD PAGE FORMAT: Name (string), reviews (stars, property)

class PropertyReviews(db.EmbeddedDocument):
    Address = db.StringField(required=True, unique=True)
    Title = db.StringField(required=True)
    Body = db.StringField(required=True)

class LandlordReviews(db.EmbeddedDocument):
    StarRating = db.IntField(required=True, min_value=0, max_value=10)
    Address = db.StringField(required=True)

class Property(db.Document):
    Category = db.StringField(required=True)
    Address = db.StringField(required=True, unique=True)
    Images = db.ImageField(required=True, unique=True, size=None, thumbnail_size=None)
    Rooms = db.IntField(required=True)
    Bathrooms = db.IntField(required=True)
    Price = db.IntField(required=True)
    LandlordName = db.StringField(required=True, unique=True)
    StarRating = db.StringField(required=True, min_value=0, max_value=10)
    Reviews = db.EmbeddedDocumentField(PropertyReviews)

class Landlord(db.Document):
    Name = db.StringFrield(required=True)
    Reviews = db.EmbeddedDocumentField(LandlordReviews)


