from typing import Literal, Dict, Optional, List
from pydantic import BaseModel, ValidationError, model_validator


class Residencial(BaseModel):
    velocidade: str
    tipo: Literal["banda larga", "fibra optica"]


class Movel(BaseModel):
    tamanho_do_plano: str
    tipo: Literal["4g", "5g"]


class Fixa(BaseModel):
    # Fixa não precisa ter detalhes
    pass


class Pacote(BaseModel):
    # Se você não quer mandar _id nunca, pode deixar como opcional:
    _id: Optional[str] = None
    
    tipo: List[Literal["Residencial", "Movel", "Fixa"]]
    cliente: Literal["Pessoa", "Empresa"]
    preco: str
    cortesia: str
    nome: str
    detalhes: Optional[Dict[Literal["Residencial", "Movel"], dict]] = None

    @model_validator(mode="before")
    @classmethod
    def validate_tipo_and_detalhes(cls, values):
        """
        Essa função será executada ANTES da validação normal dos campos (equivale a root_validator(pre=True)).
        'values' é um dicionário com todos os dados recebidos.
        """
        if not isinstance(values, dict):
            return values

        tipos = values.get("tipo", [])
        detalhes = values.get("detalhes", {})

        if not tipos:
            return values

        for t in tipos:
            if t == "Fixa":
                continue
            if t not in detalhes:
                raise ValueError(f"Detalhes para o tipo '{t}' são obrigatórios.")

            # Valida submodelo Pydantic
            if t == "Residencial":
                Residencial(**detalhes[t])
            elif t == "Movel":
                Movel(**detalhes[t])

        # Verificar se há detalhes "extras"
        for key in detalhes.keys():
            if key not in tipos:
                raise ValueError(f"Tipo '{key}' nos detalhes não está em 'tipo'.")

        return values
