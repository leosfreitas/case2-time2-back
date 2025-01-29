from pydantic import BaseModel
from typing import Literal
from typing import List, Dict, Optional

class CreatePacoteDTO(BaseModel):
    cliente: Literal["Pessoa", "Empresa"]
    tipo: List[Literal["Residencial", "Movel", "Fixa"]]
    preco: str
    cortesia: str
    nome: str
    detalhes: Optional[Dict[Literal["Residencial", "Movel"], dict]]
