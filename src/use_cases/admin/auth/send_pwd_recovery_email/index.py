from repositories.admin_repository import adminsRepository
from fastapi import FastAPI, Request, Response
from use_cases.admin.auth.send_pwd_recovery_email.send_pwd_recovery_email_use_case import SendPwdRecoveryEmailUseCase
from use_cases.admin.auth.send_pwd_recovery_email.send_pwd_recovery_email_dto import SendPwdRecoveryEmailDTO
from fastapi import APIRouter

router = APIRouter()

admin_repository = adminsRepository()
send_pwd_recovery_email_use_case = SendPwdRecoveryEmailUseCase(admin_repository)

@router.post("/admin/auth/pwd/recovery/email")
def send_pwd_recovery_email(send_pwd_recovery_email_dto: SendPwdRecoveryEmailDTO, response: Response, request: Request):
    return send_pwd_recovery_email_use_case.execute(send_pwd_recovery_email_dto, response, request)
    