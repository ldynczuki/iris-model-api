from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId

from loguru import logger


class MongoDataBase:

    def __init__(self, url: str, database: str, collection: str):
        
        self._connection = MongoClient(url)  # start mongo connection
        
        self.connection.server_info()  # test connection

        self._database = self._connection[database]  # create mongo collection
        self._collection = self._database[collection]  # create mongo document

    @property
    def connection(self):
        return self._connection

    @property
    def database(self):
        return self._database

    @property
    def collection(self):
        return self._collection

    @property
    def database_names(self):
        return self.connection.database_names()

    @property
    def collection_names(self):
        return self.database.collection_names()

    def create(self, data) -> str:
        objectid = str(self.collection.insert_one(data))
        return objectid

    def read_all(self) -> list:
        data = []
        for result in self.collection.find({}):
            result['_id'] = str(result['_id'])
            data.append(result)

        return data