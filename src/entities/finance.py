import dotenv
from pydantic import BaseModel
from typing import Literal, Optional, List
dotenv.load_dotenv()

class Finance(BaseModel):
    _id: str
    categoria: Literal["Receita", "Despesa"]
    user: str
    tipo: str
    valor: str
    data: str
    descricao: str