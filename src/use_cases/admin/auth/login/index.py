from use_cases.admin.auth.login.login_use_case import LoginUseCase
from repositories.admin_repository import adminsRepository
from fastapi import FastAPI, Request, Response
from use_cases.admin.auth.login.login_dto import LoginDTO
from fastapi import APIRouter

router = APIRouter()

admin_respository = adminsRepository()
login_use_case = LoginUseCase(admin_respository)

@router.post("/admin/auth/login")
def user_login(admin_login_dto: LoginDTO, response: Response, request: Request):
    return login_use_case.execute(admin_login_dto, response, request)