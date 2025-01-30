from fastapi import APIRouter, Request, Response
from repositories.user_repository import UsersRepository
from repositories.admin_repository import adminsRepository
from use_cases.public.auth.reset_pwd.reset_pwd_use_case import ResetPwdUseCase
from use_cases.public.auth.reset_pwd.reset_pwd_dto import ResetPwdDTO

router = APIRouter()

user_repository = UsersRepository()
admin_repository = adminsRepository()

reset_pwd_use_case = ResetPwdUseCase(user_repository, admin_repository)

@router.post("/auth/reset-password")
def reset_pwd(reset_pwd_dto: ResetPwdDTO, response: Response, request: Request):
    return reset_pwd_use_case.execute(reset_pwd_dto, response, request)
