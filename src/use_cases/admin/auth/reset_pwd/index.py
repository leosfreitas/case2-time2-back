from repositories.admin_repository import adminsRepository
from fastapi import FastAPI, Request, Response
from use_cases.admin.auth.reset_pwd.reset_pwd_use_case import ResetPwdUseCase
from use_cases.admin.auth.reset_pwd.reset_pwd_dto import ResetPwdDTO
from fastapi import APIRouter

router = APIRouter()

admin_repository = adminsRepository()
reset_pwd_use_case = ResetPwdUseCase(admin_repository)

@router.post("/admin/auth/reset/pwd")
def reset_pwd(reset_pwd_dto: ResetPwdDTO, response: Response, request: Request):
    return reset_pwd_use_case.execute(reset_pwd_dto, response, request)
    