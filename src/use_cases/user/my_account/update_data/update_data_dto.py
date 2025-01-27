from pydantic import BaseModel, ConfigDict

class UpdateDataDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    email: str
    cpf: str
    phone: str