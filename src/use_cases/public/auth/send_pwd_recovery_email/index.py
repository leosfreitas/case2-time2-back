from fastapi import APIRouter, Request, Response
from repositories.user_repository import UsersRepository
from repositories.admin_repository import adminsRepository
from use_cases.public.auth.send_pwd_recovery_email.send_pwd_recovery_email_use_case import SendPwdRecoveryEmailUseCase
from use_cases.public.auth.send_pwd_recovery_email.send_pwd_recovery_email_dto import SendPwdRecoveryEmailDTO

router = APIRouter()

user_repository = UsersRepository()
admin_repository = adminsRepository()

send_pwd_recovery_email_use_case = SendPwdRecoveryEmailUseCase(
    user_repository=user_repository, 
    admin_repository=admin_repository
)

@router.post("/auth/send-email-recovery")
def send_pwd_recovery_email(
    send_pwd_recovery_email_dto: SendPwdRecoveryEmailDTO, 
    response: Response, 
    request: Request
):
    return send_pwd_recovery_email_use_case.execute(send_pwd_recovery_email_dto, response, request)
