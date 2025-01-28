from pydantic import BaseModel

class CreateAcordoDTO(BaseModel):
    pacote_id: str
