from fastapi import Request, Response
from .create_contato_dto import CreateContatoDTO
from repositories.contato_repository import ContatoRepository
from entities.contato import Contato
import jwt
import os 

class CreateContatoUseCase:
    def __init__(self, contato_repository: ContatoRepository):
        self.contato_repository = contato_repository

    def execute(self, create_contato_dto: CreateContatoDTO, response: Response, request: Request):
        token = request.cookies.get("user_auth_token")

        payload = jwt.decode(token.split(" ")[1], os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])

        user_id = payload.get("id")
        user_email = payload.get("email")

        if not user_id:
            response.status_code = 407
            return {"status": "error", "message":"Usuário não encontrado"}

        contato = Contato(
            user_id=user_id,
            email=user_email,
            mensagem=create_contato_dto.mensagem,
            resposta=create_contato_dto.resposta
        )
        self.contato_repository.save(contato)

        response.status_code = 201
        return {
            "status": "success",
            "message": "Contato criado com sucesso"
        }
