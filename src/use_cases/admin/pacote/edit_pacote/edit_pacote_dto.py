from pydantic import BaseModel
from typing import List, Dict, Optional, Literal

class EditPacoteDTO(BaseModel):
    cliente: Optional[Literal["Pessoa", "Empresa"]]
    tipo: Optional[List[Literal["Residencial", "Movel", "Fixa"]]]
    preco: Optional[str]
    cortesia: Optional[str]
    nome: Optional[str]
    detalhes: Optional[Dict[Literal["Residencial", "Movel"], dict]]
