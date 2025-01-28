import dotenv
from pydantic import BaseModel
from typing import Literal, Optional
dotenv.load_dotenv()

class Acordo(BaseModel):
    _id: str
    user_id: str
    pacote_id: str