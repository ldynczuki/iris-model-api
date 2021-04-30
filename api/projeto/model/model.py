import pickle
import numpy as np
from projeto.settings import WEIGHTS_PATH
from loguru import logger


class Classificador():

    def __init__(self):

        self.model = pickle.load(open(WEIGHTS_PATH, 'rb'))
        
        logger.debug(self.model)

    def get_predict(self, sepal_length, sepal_width, petal_length, petal_width):
        '''
            Método para realizar a inferência dos dados enviados.
        '''
        data = np.array([[sepal_length, sepal_width, 
                          petal_length, petal_width]])

        prediction = self.model.predict(data)

        return prediction[0]