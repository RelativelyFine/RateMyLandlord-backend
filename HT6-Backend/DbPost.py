import pymongo
from ImageConvert import ConvertedImages

#PROPERTIES FORMAT: type (apartment, condo, house - string), location (address - string), images, rooms(int), bathrooms(int), price(int), LandlordName(string), StarRating (1-10 int), reviews (address, title and body -strings)
#LANDLORD REVIEW FORMAT: address, title, body - strings

#LANDLORD PAGE FORMAT: Name (string), reviews (stars, property)


client = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0.bk4dmsx.mongodb.net/?retryWrites=true&w=majority')
db = client["RateMyLandlord"]
#collection = db["Properties"]

#MODERN HOUSE
postPropertyOne = {"type": "house", "address": "Modern House Street", "images": ConvertedImages[3], "rooms": 5, "bathrooms": 3, "price": 1500, "LandlordName": "Roger Gold", "StarRating": 9, "reviews": [{"title": "Great Landlord!", "body": "Such a good first landlord, always responded on time"}, {"title": "Pretty Good", "body": "I have no complaints"}]}

#TIER TWO HOUSE
postPropertyTwo = {"type": "house", "address": "19 Princess Street", "images": ConvertedImages[2], "rooms": 4, "bathrooms": 2, "price": 1000, "LandlordName": "Roger Gold", "StarRating": 7, "reviews": [{"title": "Nice Place to stay", "body": "Really close to campus"}, {"title": "Ant Infestation in Summer", "body": "House is good unless you stay in the summer"}]}

#TIER THREE HOUSE
postPropertyThree = {"type": "house", "address": "25 Hickory Street", "images": ConvertedImages[1], "rooms": 3, "bathrooms": 1, "price": 500, "LandlordName": "John Smith", "StarRating": 8, "reviews": [{"title": "Cool House Good Price", "body": "Fun place to stay with a good Landlord"}, {"title": "The other reviews are lies", "body": "This landlord never responds, does not fix any appliances when they break"}]}

#DIRT HOUSE
postPropertyFour = {"type": "house", "address": "Dirt House Street", "images": ConvertedImages[0], "rooms": 1, "bathrooms": 0, "price": 50, "LandlordName": "John Smith", "StarRating": 9, "reviews": [{"title": "I got paid to stay here", "body": "I didn't even need a job this semester, great stay"}, {"title": "Not bad for the price", "body": "Interesting place to stay and I don't regret it"}]}

db["Properties"].insert_many([postPropertyOne, postPropertyTwo, postPropertyThree, postPropertyFour])

postLandlordOne = {"Name": "Roger Gold", "reviews": [{"stars": 8, "address": "Modern House Street"}, {"stars": 10, "address": "19 Princess Street"}]}
postLandlordTwo = {"Name": "John Smith", "reviews": [{"stars": 7, "address": "25 Hickory Street"}, {"stars": 3, "address": "Mine Craft Street"}]}

db["Landlords"].insert_many([postLandlordOne, postLandlordTwo])





#TEST SEARCH below budget

#budget = 300

#results = collection.find({'price' <= 300})

#for result in results:
    #print(result)
