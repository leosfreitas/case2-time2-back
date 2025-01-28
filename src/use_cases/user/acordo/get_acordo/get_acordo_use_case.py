# use_cases/acordo/get_acordos_by_logged_user/get_acordos_by_logged_user_use_case.py

from fastapi import Request, Response
import jwt
import os
from repositories.acordo_repository import AcordoRepository

class GetAcordosByLoggedUserUseCase:
    def __init__(self, acordo_repository: AcordoRepository):
        self.acordo_repository = acordo_repository

    def execute(self, response: Response, request: Request):
        token = request.cookies.get("user_auth_token")
        if not token:
            response.status_code = 401
            return {"status": "error", "message": "Token de autenticação não encontrado"}

        try:
            # Exemplo: token no cookie vem "Bearer <jwt>", por isso split()[1]
            payload = jwt.decode(
                token.split(" ")[1],
                os.getenv("USER_JWT_SECRET"),
                algorithms=["HS256"]
            )
        except (jwt.DecodeError, IndexError):
            response.status_code = 401
            return {"status": "error", "message": "Token inválido ou ausente"}

        user_id = payload.get("id")
        if not user_id:
            response.status_code = 404
            return {"status": "error", "message": "Usuário não encontrado no token"}

        # Busca todos os acordos do usuário
        acordos = self.acordo_repository.get_acordos_by_user_id(user_id)

        response.status_code = 200
        return acordos
