from fastapi import APIRouter, Path
from projeto.responses.database import DatabaseResponse
from projeto.database.database import Iris


router = APIRouter()


@router.get('/get_predict', status_code=200, response_model=DatabaseResponse, summary="Retorna os dados armazenados no Banco de Dados")
def listar():
    """Retorna os dados armazenados no Banco de Dados"""
    return {"resultado": Iris().listar()}
