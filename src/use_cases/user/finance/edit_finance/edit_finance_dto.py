from pydantic import BaseModel
from typing import Literal, Optional

class EditFinanceDTO(BaseModel):
    tipo: str
    valor: Optional[str]  
    data: Optional[str]  
    descricao: Optional[str]
