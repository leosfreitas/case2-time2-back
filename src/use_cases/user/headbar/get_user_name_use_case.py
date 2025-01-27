from repositories.user_repository import UsersRepository
from fastapi import Request, Response

class getUserName:
    def __init__(self, user_repository: UsersRepository) -> None:
        self.user_repository = user_repository

    def execute(self, response: Response, request:Request):
        user_id = request.state.auth_payload["user_id"]
        user_name = self.user_repository.get_name(user_id)

        return {"status":"success", "user_name":user_name}