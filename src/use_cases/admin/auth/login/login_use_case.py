from repositories.admin_repository import adminsRepository
from fastapi import FastAPI, Request, Response
from use_cases.admin.auth.login.login_dto import LoginDTO
from entities.admin import Admin
import datetime
import jwt
import os

class LoginUseCase:
    admin_repository: adminsRepository

    def __init__(self, admin_repository: adminsRepository):
        self.admin_repository = admin_repository

    def execute(self, login_dto: LoginDTO, response: Response, request: Request):
        check_exists = self.admin_repository.find_by_email(email=login_dto.email)

        if (len(check_exists) == 0):
            response.status_code = 404
            return {"status": "error", "message": "Não foi possível achar um admin com o email fornecido"}

        admin = check_exists[0]

        if (not admin.check_password_matches(login_dto.password)):
            response.status_code = 400
            return {"status": "error", "message": "Senha incorreta, tente novamente mais tarde."}
        
        expiration = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=90)

        token = jwt.encode({"email": admin.email, "id": str(admin.id)}, os.getenv("ADMIN_JWT_SECRET"))
        
        response.set_cookie(
            key="admin_auth_token",
            value=f"Bearer {token}",
            httponly=True,
            expires=expiration,
            secure=False,
            domain="localhost",  
        )


        response.status_code = 202
        return {"status": "success", "message": "Acesso permitido"}