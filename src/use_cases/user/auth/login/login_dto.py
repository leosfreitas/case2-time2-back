from pydantic import BaseModel
from typing import Literal

class LoginDTO(BaseModel):
    email: str
    password: str
