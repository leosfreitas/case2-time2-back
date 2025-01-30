from repositories.user_repository import UsersRepository
from fastapi import Request, Response

class GetUserData:
    def __init__(self, user_repository: UsersRepository) -> None:
        self.user_repository = user_repository

    def execute(self, response: Response, request: Request):
        user_id = request.state.auth_payload["user_id"]
        user_tipo = self.user_repository.get_tipo(user_id)
        user_name = self.user_repository.get_name(user_id)
        user_email = self.user_repository.get_email(user_id)
        user_phone = self.user_repository.get_phone(user_id)

        user_cpf = None
        user_cnpj = None

        if user_tipo == "Pessoa":
            user_cpf = self.user_repository.get_cpf(user_id)
        elif user_tipo == "Empresa":
            user_cnpj = self.user_repository.get_cnpj(user_id)

        user_data = {
            "tipo": user_tipo,
            "name": user_name,
            "email": user_email,
            "phone": user_phone,
            "id": user_id,
        }

        if user_cpf:
            user_data["cpf"] = user_cpf

        if user_cnpj:
            user_data["cnpj"] = user_cnpj

        return {"status": "success", "data": user_data}
