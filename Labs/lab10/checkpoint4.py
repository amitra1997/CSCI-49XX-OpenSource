import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId

if __name__ == '__main__':
	db = MongoClient().mongo_db_lab
	definitions = db.definitions
	print("Fetch all records")
	for q in definitions.find():
		pprint.pprint(q)
	print("Fetch one record")
	pprint.pprint(definitions.find_one())
	print("Fetch a specific record")
	pprint.pprint(definitions.find_one({"word":"Time"}))
	print("Fetch a record by object id")
	pprint.pprint(definitions.find_one({"_id": ObjectId("5ca79171a331ad2eed76238e")}))
	print("Insert a new record")
	pprint.pprint(definitions.insert({"word": "Aditya", "definition": "Greatest name in the world."}))