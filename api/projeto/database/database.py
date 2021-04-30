from projeto.database import MongoDataBase
from projeto.settings import MONGODB_URL, MONGODB_DATABASE, MONGODB_COLLECTION


class Iris():

    def listar(self):
        
        database = MongoDataBase(MONGODB_URL, MONGODB_DATABASE, MONGODB_COLLECTION)
        response = database.read_all()

        return response
    

    def inserir(self, sepal_length, sepal_width, 
                petal_length, petal_width, response_clf):

        database = MongoDataBase(MONGODB_URL, MONGODB_DATABASE, MONGODB_COLLECTION)
        response = database.create({'sepal_length': sepal_length, 'sepal_width': sepal_width, 
                                    'petal_length': petal_length, 'petal_width': petal_width, 
                                    'classe': response_clf})

        return response