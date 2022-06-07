from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
from flask_cors import CORS

SITE_NAME = "http://localhost:3000"
app = Flask(__name__)
api = Api(app)
CORS(app)

# [{"id":1,"category":"Product","name":"Passion Fruit","imageUrl":"assets/products/passionfuit.png"},
# {"id":2,"category":"Interest","name":"Surf","imageUrl":"assets/interests/surf.png"},
# {"id":3,"category":"Lifestyle","name":"Nutrition","imageUrl":"assets/lifestyle/nutrition.png"},
# {"id":4,"category":"Athlete","name":"Paul Rodriguex", "sport": "Skateboarder", "awards": "Eight-time X Games Medalist, Actor", "imageUrl":"assets/athletes/prod.png"}]


products2 = [
  {
        "product_id": 1,
        "category": "Product",
        "name": "Passion Fruit",
        "product_attributes": {
            "line": "ashoc",
            "type": "shoes",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/can-01_9c9aedd3-dddd-44c5-a2ae-5c59094d04a2_350x.png?v=1644872374xs"
    },
    {
        "product_id": 2,
        "category": "Product",
        "name": "Citrus Ice",
        "product_attributes": {
            "line": "ashoc",
            "type": "shoes",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/can-02_761ce601-d856-4406-874c-e2d387d2174d_350x.png?v=1644872388"
    },
    {
        "product_id": 3,
        "category": "Product",
        "name": "Watermelon",
        "product_attributes": {
            "line": "ashoc",
            "type": "shoes",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/can-05_7914e437-fbd4-458b-bad6-48dae99d3bc1_350x.png?v=1644872416"
    },
    {
        "product_id": 21,
        "category": "athlete",
        "name": "Paul Rodriguez P-ROD",
        "product_attributes": {
            "sport": "Skateboarder",
            "accolades": "Eight-time X Games Medalist, Actor",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/prod2_786dd702-160c-4c30-a306-f37bee487e7e_350x.png?v=1644873410"
    },
    {
        "product_id": 22,
        "category": "athlete",
        "name": "Chase Elliot",
        "product_attributes": {
            "sport": "Race Car Driver",
            "accolades": "2020 NASCAR Cup Series Champion",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/a_shoc_athlete-sliced_03_d6bf12ca-dda3-49ca-973a-e8c84417e54d_350x.png?v=1644873439"
    },
    {
        "product_id": 23,
        "category": "athlete",
        "name": "Billy Kemper",
        "product_attributes": {
            "sport": "Surfer",
            "accolades": "WSL Big Wave World Champion",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/a_shoc_athlete-sliced_05_2_350x.png?v=1644873462"
    },
    {
        "product_id": 24,
        "category": "athlete",
        "name": "Loui Vito",
        "product_attributes": {
            "sport": "Snowboarder",
            "accolades": "Olympian, Winter X Games Medalist, Grand Prix Champion",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/a_shoc_athlete-sliced_07_1_350x.png?v=1644873497"
    },
    {
        "product_id": 25,
        "category": "athlete",
        "name": "Ryan Hall",
        "product_attributes": {
            "sport": "Endurance Athlete",
            "accolades": "2X Olympian + Fastest Marathon by an American",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/a_shoc_athlete-sliced_09_1_350x.png?v=1644873519"
    },
        {
        "product_id": 26,
        "category": "athlete",
        "name": "Matty Hong",
        "product_attributes": {
            "sport": "Climber",
            "accolades": "Fourth American to climb 5.15b Fight or Flight; Oliana, Spain",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/a_shoc_athlete-sliced_17_1_350x.png?v=1644873555"
    }
]

products1 = [
    {
        "product_id": 1,
        "category": "Product",
        "name": "Passion Fruit",
        "product_attributes": {
        	"line": "ashoc",
        	"type": "shoes",
        	"style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/can-01_9c9aedd3-dddd-44c5-a2ae-5c59094d04a2_350x.png?v=1644872374xs"
    },
    {
        "product_id": 2,
        "category": "Product",
        "name": "Citrus Ice",
        "product_attributes": {
            "line": "ashoc",
            "type": "shoes",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/can-02_761ce601-d856-4406-874c-e2d387d2174d_350x.png?v=1644872388"
    },
        {
        "product_id": 2,
        "category": "Product",
        "name": "Fruit Punch",
        "product_attributes": {
            "line": "ashoc",
            "type": "shoes",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/can-04_6a063c9b-59fe-4bf2-99c6-faa46abea71d_350x.png?v=1644872400"
    },
    {
        "product_id": 3,
        "category": "Product",
        "name": "Watermelon",
        "product_attributes": {
            "line": "ashoc",
            "type": "shoes",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/can-05_7914e437-fbd4-458b-bad6-48dae99d3bc1_350x.png?v=1644872416"
    },
    {
        "product_id": 4,
        "category": "Product",
        "name": "Acai Berry",
        "product_attributes": {
            "line": "ashoc",
            "type": "shoes",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/can-07_31d28181-f211-433f-a01c-312de591b9d0_350x.png?v=1644872436"
    },
    {
        "product_id": 5,
        "category": "Product",
        "name": "Peach Mango",
        "product_attributes": {
            "line": "ashoc",
            "type": "shoes",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/can-08_bc3f0980-6d86-456c-8cd0-997f692b0477_350x.png?v=1644872772"
    },
    {
        "product_id": 6,
        "category": "Product",
        "name": "Blue Raspberry",
        "product_attributes": {
            "line": "ashoc",
            "type": "shoes",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/can-06_a36754cd-95aa-4397-a569-e3ae3f742bd0_350x.png?v=1644872787"
    },
    {
        "product_id": 7,
        "category": "Product",
        "name": "Orange Freeze",
        "product_attributes": {
            "line": "ashoc",
            "type": "shoes",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/can-03_91baeae2-76a5-46a2-8030-59d07b5d6b26_350x.png?v=1644872799"
    },
    {
        "product_id": 8,
        "category": "Product",
        "name": "Orange Mango",
        "product_attributes": {
            "line": "accelerator",
            "type": "shoes",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/accelerator_OrangeMango_can-01_a3e2470f-a939-49c1-85ee-016ca2765eb8_350x.jpg?v=1645161582"
    },
    {
        "product_id": 9,
        "category": "Product",
        "name": "Cherry Limeade",
        "product_attributes": {
            "line": "accelerator",
            "type": "shoes",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/accelerator_cherry_limeade_12_350x.jpg?v=1645161615"
    },
    {
        "product_id": 10,
        "category": "Product",
        "name": "Island Guava",
        "product_attributes": {
            "line": "accelerator",
            "type": "shoes",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/accelerator_Island_Guava_can-03_087f144a-cd43-4b5f-8fbf-6f2f0d791ee2_350x.jpg?v=1645161650"
    },
    {
        "product_id": 10,
        "category": "Product",
        "name": "Kiwi Lime",
        "product_attributes": {
            "line": "accelerator",
            "type": "shoes",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/accelerator_Kiwi_Lime_can-01_2_350x.jpg?v=1645167608"
    }
]

products = [
    {
        "product_id": 11,
        "category": "Interest: Lifestyle",
        "name": "Dieting",
        "product_attributes": {
            "color": "black",
        },
        "image_link": SITE_NAME + "/cards/interests/lifestyle/dieting.png"
    },
    {
        "product_id": 12,
        "category": "Interest: Sports",
        "name": "NBA",
        "product_attributes": {
            "color": "black",
        },
        "image_link": SITE_NAME + "/cards/interests/sports/NBA.png"
    },
    {
        "product_id": 12,
        "category": "Interest: Lifestyle",
        "name": "Nutrition",
        "product_attributes": {
            "color": "black",
        },
        "image_link": SITE_NAME + "/cards/interests/lifestyle/nutrition.png"
    },
    {
        "product_id": 12,
        "category": "Interest: Sports",
        "name": "NFL",
        "product_attributes": {
            "color": "black",
        },
        "image_link": SITE_NAME + "/cards/interests/sports/NFL.png"
    },
    {
        "product_id": 12,
        "category": "Interest: Lifestyle",
        "name": "Natural-Products",
        "product_attributes": {
            "color": "black",
        },
        "image_link": SITE_NAME + "/cards/interests/lifestyle/natural-products.png"
    },
    {
        "product_id": 12,
        "category": "Interest: Sports",
        "name": "Surf",
        "product_attributes": {
            "color": "black",
        },
        "image_link": SITE_NAME + "/cards/interests/sports/surf.png"
    },
    {
        "product_id": 12,
        "category": "Interest: Lifestyle",
        "name": "Energy",
        "product_attributes": {
            "color": "black",
        },
        "image_link": SITE_NAME + "/cards/interests/lifestyle/energy.png"
    },
    {
        "product_id": 12,
        "category": "Athelete: Nascar",
        "name": "Chase Elliot",
        "product_attributes": {
            "color": "black",
        },
        "image_link": SITE_NAME + "/cards/athletes/chase-elliott.png"
    }
]

lifestyle = [
    {
        "product_id": 17,
        "category": "lifestyle",
        "name": "Nutrition",
        "product_attributes": {
            "color": "black",
            "type": "shoes",
            "style": "high",
        },
        "image_link": SITE_NAME + "/cards/athletes/prod.png"
    },
    {
        "product_id": 18,
        "category": "lifestyle",
        "name": "Natural",
        "product_attributes": {
            "color": "black",
            "type": "shoes",
            "style": "high",
        },
        "image_link": SITE_NAME + "/cards/athletes/prod.png"
    },
   {
        "product_id": 19,
        "category": "lifestyle",
        "name": "Energy",
        "product_attributes": {
            "color": "black",
            "type": "shoes",
            "style": "high",
        },
        "image_link": SITE_NAME + "/cards/athletes/prod.png"
    },
   {
        "product_id": 20,
        "category": "lifestyle",
        "name": "Dieting",
        "product_attributes": {
            "color": "black",
            "type": "shoes",
            "style": "high",
        },
        "image_link": SITE_NAME + "/cards/athletes/prod.png"
    }
]

athletes = [
    {
        "product_id": 21,
        "category": "athlete",
        "name": "Paul Rodriguez P-ROD",
        "product_attributes": {
            "sport": "Skateboarder",
            "accolades": "Eight-time X Games Medalist, Actor",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/prod2_786dd702-160c-4c30-a306-f37bee487e7e_350x.png?v=1644873410"
    },
    {
        "product_id": 22,
        "category": "athlete",
        "name": "Chase Elliot",
        "product_attributes": {
            "sport": "Race Car Driver",
            "accolades": "2020 NASCAR Cup Series Champion",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/a_shoc_athlete-sliced_03_d6bf12ca-dda3-49ca-973a-e8c84417e54d_350x.png?v=1644873439"
    },
    {
        "product_id": 23,
        "category": "athlete",
        "name": "Billy Kemper",
        "product_attributes": {
            "sport": "Surfer",
            "accolades": "WSL Big Wave World Champion",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/a_shoc_athlete-sliced_05_2_350x.png?v=1644873462"
    },
    {
        "product_id": 24,
        "category": "athlete",
        "name": "Loui Vito",
        "product_attributes": {
            "sport": "Snowboarder",
            "accolades": "Olympian, Winter X Games Medalist, Grand Prix Champion",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/a_shoc_athlete-sliced_07_1_350x.png?v=1644873497"
    },
    {
        "product_id": 25,
        "category": "athlete",
        "name": "Ryan Hall",
        "product_attributes": {
            "sport": "Endurance Athlete",
            "accolades": "2X Olympian + Fastest Marathon by an American",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/a_shoc_athlete-sliced_09_1_350x.png?v=1644873519"
    },
        {
        "product_id": 26,
        "category": "athlete",
        "name": "Matty Hong",
        "product_attributes": {
            "sport": "Climber",
            "accolades": "Fourth American to climb 5.15b Fight or Flight; Oliana, Spain",
            "style": "high",
        },
        "image_link": "https://cdn.shopify.com/s/files/1/0071/3369/1957/files/a_shoc_athlete-sliced_17_1_350x.png?v=1644873555"
    }
]

class Feedback(Resource):

	def post(self, id):
		parser = reqparse.RequestParser()
		parser.addArgument("did_like")
		params = parser.parser_args()

		global products
		products = [product for product in products if product["product_id"] != id]
		return "Products with id {id} was downvoted", 200


class Product(Resource):

	def get(self, id=0):
		return products

	# def post(self, id):
	# 	parser = reqparse.RequestParser()
	# 	parser.addArgument("author")
	# 	parser.addArgument("quote")
	# 	params = parser.parser_args()

	# 	for quote in ai_quotes:
	# 		if(id == quote["id"]):
	# 			return f"Quote with id {id} already exists", 400

	# 	quote = {
	# 		"id": int(id),
	# 		"author": params["author"],
	# 		"quote": params["quote"]
	# 	}
	# 	ai_quotes.append(quote)
	# 	return quote, 201

	# def put(self, id):
	# 	parser = reqparse.RequestParser()
	# 	parser.addArgument("author")
	# 	parser.addArgument("quote")
	# 	params = parser.parser_args()

	# 	for quote in ai_quotes:
	# 		if(id == quote["id"]):
	# 			quote["author"] = params["author"]
	# 			quote["quote"] = params["quote"]
	# 			return quote, 200

	# 	quote = {
	# 		"id": id,
	# 		"author": params["author"],
	# 		"quote": params["quote"]
	# 	}

	# 	ai_quotes.append(quote)
	# 	return quote, 201

	# def delete(self, id):
	# 	global ai_quotes
	# 	ai_quotes = [qoute for qoute in ai_quotes if qoute["id"] != id]
	# 	return f"Quote with id {id} is deleted.", 200

api.add_resource(Product, "/products", "/products/", "/products/<int:id>")
api.add_resource(Feedback, "/feedback", "/feedback", "/feedback/<int:id>")
if __name__ == '__main__':
    app.run(debug=True)



