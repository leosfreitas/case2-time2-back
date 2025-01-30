import os
import jwt
from fastapi import Request, Response
from repositories.user_repository import UsersRepository

class DeleteUserUseCase:
    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    def execute(self, user_id: str, response: Response, request: Request):
        user_deleted = self.user_repository.delete_user_by_id(user_id)
    
        if not user_deleted:
            response.status_code = 404
            return {"status": "error", "message": f"User com ID {user_id} não encontrado"}

        response.status_code = 200
        return {"status": "success", "message": f"User com ID {user_id} deletado com sucesso"}
