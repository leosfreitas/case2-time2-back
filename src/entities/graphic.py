from pydantic import BaseModel
from typing import Dict, List

class Graphic(BaseModel):
    dados: Dict[str, float]


