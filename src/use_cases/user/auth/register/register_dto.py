from typing import Literal, Optional
from pydantic import BaseModel, EmailStr, Field, model_validator


class RegisterDTO(BaseModel):
    tipo: Literal["Pessoa", "Empresa"]
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)
    cpf: Optional[str] = None  # CPF para Pessoa
    cnpj: Optional[str] = None  # CNPJ para Empresa
    phone: str = Field(..., min_length=10, max_length=15)

    @model_validator(mode="before")
    @classmethod
    def validate_cpf_or_cnpj(cls, values):
        """
        Valida o CPF ou CNPJ com base no tipo do usuário antes da validação normal.
        """
        tipo = values.get("tipo")
        cpf = values.get("cpf")
        cnpj = values.get("cnpj")

        # Validações para tipo "Pessoa"
        if tipo == "Pessoa":
            if not cpf:
                raise ValueError("O campo 'cpf' é obrigatório para usuários do tipo 'Pessoa'.")
            if cnpj:
                raise ValueError("Usuários do tipo 'Pessoa' não devem ter o campo 'cnpj'.")

        # Validações para tipo "Empresa"
        elif tipo == "Empresa":
            if not cnpj:
                raise ValueError("O campo 'cnpj' é obrigatório para usuários do tipo 'Empresa'.")
            if cpf:
                raise ValueError("Usuários do tipo 'Empresa' não devem ter o campo 'cpf'.")

        return values

    class Config:
        """
        Configuração para permitir limpeza de espaços e outros ajustes.
        """
        anystr_strip_whitespace = True
