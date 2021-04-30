from typing import List
from pydantic import BaseModel, Field


class Database(BaseModel):
    _id: str = Field(..., description='Id do objeto armazenado')
    sepal_length: float = Field(..., description='Valor do comprimento da sepala em centimetros')
    sepal_width: float = Field(..., description='Valor da largura da sepala em centimetros')
    petal_length: float = Field(..., description='Valor do comprimento da petala em centimetros')
    petal_width: float = Field(..., description='Valor da largura da petala em centimetros')
    classe: str = Field(..., description='Classificacao da flor')

class DatabaseResponse(BaseModel):
    resultado: List[Database] = Field(..., description='Lista objetos armazenados no banco de dados')