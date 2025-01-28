from pydantic import BaseModel
from typing import Optional

class CreateContatoDTO(BaseModel):
    mensagem: str
    resposta: Optional[str]
