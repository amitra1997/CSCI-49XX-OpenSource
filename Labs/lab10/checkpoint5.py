import pprint
import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    db = MongoClient().mongo_db_lab
    randWord = db.definitions.aggregate([{"$sample": { "size": 1}}]).next()
    print("before update")
    db.definitions.update(randWord, {"$push": {"dates": datetime.datetime.utcnow()}})
    pprint.pprint(randWord)
    return None

if __name__ == '__main__':
    print random_word_requester()
