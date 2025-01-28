import dotenv
from pydantic import BaseModel
from typing import Literal, Optional, List
dotenv.load_dotenv()

class Sac(BaseModel):
    _id: str
    nome: str
    email: str
    motivo: str
    mensagem: str
    resposta: Optional[str]