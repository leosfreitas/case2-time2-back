import dotenv
from pydantic import BaseModel
from typing import Literal
dotenv.load_dotenv()

class Budget(BaseModel):
    _id: str
    user: str
    tipo: Literal[
    "Habitação",
    "Transporte",
    "Alimentação",
    "Saúde",
    "Educação",
    "Lazer",
    "Roupas",
    "Tecnologia",
    "Assinaturas e Serviços",
    "Investimentos",
    "Doações",
    "Impostos",
    "Dívidas",
    "Outros"
    ]
    valor: str
