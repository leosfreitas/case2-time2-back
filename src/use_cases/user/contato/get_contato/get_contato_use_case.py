from repositories.contato_repository import ContatoRepository
from fastapi import Request, Response
import os
import jwt

class GetContatoUseCase:
    def __init__(self, contatos_repository: ContatoRepository):
        self.contatos_repository = contatos_repository

    def execute(self, response: Response, request: Request):
        token = request.cookies.get("user_auth_token")
        try:
            payload = jwt.decode(token.split(" ")[1], os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])
            user_id = payload.get("id")
        except (jwt.DecodeError, IndexError, AttributeError):
            response.status_code = 401
            return {"status": "error", "message": "Invalid or missing token"}

        if not user_id:
            response.status_code = 404
            return {"status": "error", "message": "Usuário não encontrado"}

        contato = self.contatos_repository.get_all_contatos_by_user_id(user_id)
        if not contato:
            response.status_code = 404
            return {"status": "error", "message": "Nenhum contato encontrado."}

        response.status_code = 200
        return contato