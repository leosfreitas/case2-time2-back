from pydantic import BaseModel
from typing import Literal, Optional

class CreateSacDTO(BaseModel):
    nome: str
    email: str
    motivo: str
    mensagem: str
    resposta: Optional[str]