from fastapi import Request, Response
from .create_acordo_dto import CreateAcordoDTO
from repositories.acordo_repository import AcordoRepository
from entities.acordo import Acordo
import jwt
import os

class CreateAcordoUseCase:
    def __init__(self, acordo_repository: AcordoRepository):
        self.acordo_repository = acordo_repository

    def execute(self, create_acordo_dto: CreateAcordoDTO, response: Response, request: Request):

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

        acordo = Acordo(
            user_id=user_id,
            pacote_id=create_acordo_dto.pacote_id
        )

        self.acordo_repository.save(acordo)

        response.status_code = 201
        return {
            "status": "success",
            "message": "Acordo criado com sucesso"
        }
