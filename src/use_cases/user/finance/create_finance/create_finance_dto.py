from pydantic import BaseModel
from typing import Literal, Optional

class CreateFinanceDTO(BaseModel):
    categoria: Literal[
        "Receita",
        "Despesa"
    ]
    
    tipo: str
    valor: str
    data: str
    descricao: str