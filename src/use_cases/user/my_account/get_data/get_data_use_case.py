from repositories.user_repository import UsersRepository
from fastapi import Request, Response

class getUserData:
    def __init__(self, user_repository: UsersRepository) -> None:
        self.user_repository = user_repository

    def execute(self, response: Response, request: Request):
        user_id = request.state.auth_payload["user_id"]
        user_name = self.user_repository.get_name(user_id)
        user_email = self.user_repository.get_email(user_id)
        user_cpf = self.user_repository.get_cpf(user_id)
        user_phone = self.user_repository.get_phone(user_id)

        return {"status":"success", "data": {"name": user_name, 
                                             "email": user_email, 
                                             "cpf": user_cpf,
                                             "phone": user_phone,
                                             "id": user_id}}