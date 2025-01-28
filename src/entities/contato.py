import dotenv
from pydantic import BaseModel
from typing import Literal, Optional
dotenv.load_dotenv()

class Contato(BaseModel):
    _id: str
    user_id: str
    email: str
    mensagem: str
    resposta: Optional[str]