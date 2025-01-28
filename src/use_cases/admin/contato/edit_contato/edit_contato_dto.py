from pydantic import BaseModel

class EditContatoDTO(BaseModel):
    mensagem: str
