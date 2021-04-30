from fastapi import APIRouter, Request, Query
from projeto.model.model import Classificador
from projeto.responses.responses import IrisResponse
from projeto.database.database import Iris


router = APIRouter()
model = Classificador()

@router.get('/health', status_code=200, summary="Verifica se o endpoint está funcional")
def listar():
    """Verifica se o endpoint está funcional"""
    return {"resultado": "OK"}


@router.post('/predict', status_code=200, response_model=IrisResponse, summary="Realiza a classificação de flores")
def inserir(request: Request,
            sepal_length: float = Query(..., description="Valor do comprimento da sépala em centímetros"),
            sepal_width: float = Query(..., description="Valor da largura da sépala em centímetros"),
            petal_length: float = Query(..., description="Valor do comprimento da pétala em centímetros"),
            petal_width: float = Query(..., description="Valor da largura da pétala em centímetros")):
    """Realiza a classificação de flores"""

    response_clf = model.get_predict(sepal_length, sepal_width, petal_length, petal_width)
    inserir_db = Iris().inserir(sepal_length, sepal_width, petal_length, petal_width, response_clf)

    return {"resultado": response_clf}