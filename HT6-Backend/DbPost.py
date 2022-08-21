import pymongo
from ImageConvert import ConvertedImages

CLIENT = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0.bk4dmsx.mongodb.net/?retryWrites=true&w=majority')
DB = CLIENT["RateMyLandlord"]
#collection = db["Properties"]

    #Category = db.StringField(required=True)
    #Address = db.StringField(required=True, unique=True)
    #Images = db.ImageField(required=True, unique=True, size=None, thumbnail_size=None)
    #Rooms = db.IntField(required=True)
    #Bathrooms = db.IntField(required=True)
    #Price = db.IntField(required=True)
    #LandlordName = db.StringField(required=True)
    #StarRating = db.StringField(required=True, min_value=0, max_value=10)
    #Reviews = db.EmbeddedDocumentField(PropertyReviews)

#MODERN HOUSE
postPropertyOne = {"Category": "house", "Address": "Modern House Street", "Campus": "Queens", "Images": ConvertedImages[3], "Rooms": 5, "Bathrooms": 3, "Price": 1500, "LandlordName": "Roger Gold", "StarRating": 9, "Reviews": [{"Title": "Great Landlord!", "Body": "Such a good first landlord, always responded on time"}, {"Title": "Pretty Good", "Body": "I have no complaints"}]}

#TIER TWO HOUSE
postPropertyTwo = {"Category": "house", "Address": "19 Princess Street", "Campus": "Laurier", "Images": ConvertedImages[2], "Rooms": 4, "Bathrooms": 2, "Price": 1000, "LandlordName": "Roger Gold", "StarRating": 7, "Reviews": [{"Title": "Nice Place to stay", "Body": "Really close to campus"}, {"Title": "Ant Infestation in Summer", "Body": "House is good unless you stay in the summer"}]}

#TIER THREE HOUSE
postPropertyThree = {"Category": "house", "Address": "25 Hickory Street", "Campus": "Queens", "Images": ConvertedImages[1], "Rooms": 3, "Bathrooms": 1, "Price": 500, "LandlordName": "John Smith", "StarRating": 8, "Reviews": [{"Title": "Cool House Good Price", "Body": "Fun place to stay with a good Landlord"}, {"Title": "The other reviews are lies", "Body": "This landlord never responds, does not fix any appliances when they break"}]}

#DIRT HOUSE
postPropertyFour = {"Category": "house", "Address": "Dirt House Street", "Campus": "Brock", "Images": ConvertedImages[0], "Rooms": 1, "Bathrooms": 0, "Price": 50, "LandlordName": "John Smith", "StarRating": 9, "Reviews": [{"Title": "I got paid to stay here", "Body": "I didn't even need a job this semester, great stay"}, {"Title": "Not bad for the price", "Body": "Interesting place to stay and I don't regret it"}]}

DB["Properties"].insert_many([postPropertyOne, postPropertyTwo, postPropertyThree, postPropertyFour])

postLandlordOne = {"Name": "Roger Gold", "Reviews": [{"Stars": 8, "Address": "Modern House Street"}, {"Stars": 10, "Address": "19 Princess Street"}]}
postLandlordTwo = {"Name": "John Smith", "Reviews": [{"Stars": 7, "Address": "25 Hickory Street"}, {"Stars": 3, "Address": "Mine Craft Street"}]}

DB["Landlords"].insert_many([postLandlordOne, postLandlordTwo])





#TEST SEARCH below budget

#budget = 300

#results = collection.find({'price' <= 300})

#for result in results:
    #print(result)
