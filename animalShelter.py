from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, **kwargs):
        # Initializing the MongoClient. Capture keyword arguments supplied by user. 
        self.client = MongoClient('mongodb://%s:%s@localhost:54766/AAC' % (kwargs['username'], kwargs['password']))
        # Port number entered.
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
           #Original work commented out and replaced with specific true and false per module instructions
            #return self.database.animals.insert(data)  # data should be dictionary            
            #else:
            #raise Exception("Nothing to save, because data parameter is empty")
            try:
                self.database.animals.insert(data)
                return True
            except: 
                return False
        else: 
            return False
# Create method to implement the R in CRUD. 
#Read method result in cursor if successful, return error if not.
    def read(self, query):
        if query is not None:
            return self.database.animals.find(query, {"_id": False}) #ID false added to eliminate error.
        else:
            raise Exception("No query specified.") # Returns error if query is not provided.

    #Create method result in JSON format if successful, return error if not.            
    def update(self, query, data):
        if query is None:
            raise Exception("Query not specified.")
        if data is None:
            raise Exception("Data not specified.")
            
        results = self.database.animals.update_many(query,data)
        return dumps(results.raw_result)

    #Create delete method return JSON format if successful, return error if not.
    def delete(self, query):
        if query is None:
            raise Exception("Query not specified.")
            
        results = self.database.animals.delete_many(query)
        return dumps(results.raw_result)
   