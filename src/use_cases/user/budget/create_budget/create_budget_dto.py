from pydantic import BaseModel
from typing import Literal

class CreateBudgetDTO(BaseModel):
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
