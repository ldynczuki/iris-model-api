from typing import List
from pydantic import BaseModel, Field


class IrisResponse(BaseModel):
    resultado: str = Field(..., description='Resultado da classificação')