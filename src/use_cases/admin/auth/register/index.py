from use_cases.user.auth.register.register_use_case import RegisterUseCase
from repositories.admin_repository import adminsRepository
from fastapi import FastAPI, Request, Response
from use_cases.admin.auth.register.register_dto import RegisterDTO
from fastapi import APIRouter

router = APIRouter()

admin_repository = adminsRepository()
admin_register_use_case = RegisterUseCase(admin_repository)

@router.post("/admin/auth/register")
def admin_register(register_dto: RegisterDTO, response: Response, request: Request):
    return admin_register_use_case.execute(register_dto, response, request)
    