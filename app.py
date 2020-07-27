from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)


products = [
    {
        "product_id": 1,
        "product_name": "Sk8-Hi Pro BMX",
        "product_attributes": {
        	"color": "black",
        	"type": "shoes",
        	"style": "high",
        },
        "image_link": "https://images.vans.com/is/image/Vans/VHGB9M-HERO?$WC-FULLIMAGE$"
    },
    {
        "product_id": 2,
        "product_name": "Rowan Pro",
        "product_attributes": {
        	"color": "white",
        	"type": "shoes",
        	"style": "low",
        },
        "image_link": "https://images.vans.com/is/image/Vans/TZCW8S-HERO?$WC-FULLIMAGE$"
    },
    {
        "product_id": 3,
        "product_name": "Mirage Rowan Pro",
        "product_attributes": {
        	"color": "blue",
        	"type": "shoes",
        	"style": "low",
        },
        "image_link": "https://images.vans.com/is/image/Vans/TZCW5J-HERO?$WC-FULLIMAGE$"
    },
    {
        "product_id": 4,
        "product_name": "Berle Pro",
        "product_attributes": {
        	"color": "blue",
        	"type": "shoes",
        	"style": "low",
        },
        "image_link": "https://images.vans.com/is/image/Vans/WKXFS1-HERO?$WC-FULLIMAGE$"
    },
    {
        "product_id": 5,
        "product_name": "Slip On",
        "product_attributes": {
        	"color": "white",
        	"type": "shoes",
        	"style": "slip",
        },
        "image_link": "https://images.vans.com/is/image/Vans/EYEW00-HERO?$WC-FULLIMAGE$"
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



