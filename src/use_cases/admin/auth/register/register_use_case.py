from repositories.admin_repository import adminsRepository
from use_cases.user.auth.register.register_dto import RegisterDTO
from fastapi import Request, Response
from entities.user import User

class RegisterUseCase:
    admin_repository = adminsRepository

    def __init__(self, admin_repository: adminsRepository):
        self.admin_repository = admin_repository

    def execute(self, register_dto: RegisterDTO, response: Response, request: Request):
        if not register_dto.name or not register_dto.email or not register_dto.password:
            response.status_code = 406
            return{"status": "error", "message": "Cadastro não realizado, pois falta informações"}

        user = User(**register_dto.model_dump())

        self.admin_repository.save(user)

        response.status_code = 201

        return{"status": "success", "message": "Cadastro do usuário realizado com sucesso"}