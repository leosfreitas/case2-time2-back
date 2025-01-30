from repositories.user_repository import UsersRepository
from repositories.admin_repository import adminsRepository
from fastapi import Request, Response
from use_cases.public.auth.reset_pwd.reset_pwd_dto import ResetPwdDTO
from datetime import datetime

class ResetPwdUseCase:
    def __init__(self, user_repository: UsersRepository, admin_repository: adminsRepository):
        self.user_repository = user_repository
        self.admin_repository = admin_repository

    def _find_user_in_any_repo_by_token(self, token: str):
        user = self.user_repository.find_by_reset_pwd_token(token=token)
        if user and len(user) > 0:
            return (user[0], "user")

        admin = self.admin_repository.find_by_reset_pwd_token(token=token)
        if admin and len(admin) > 0:
            return (admin[0], "admin")

        return (None, None)

    def _update_password_and_clear_token(
        self, 
        user_type: str,
        user_id: int, 
        user_email: str, 
        new_password: str
    ):
        if user_type == "user":
            self.user_repository.update_pwd(user_id, new_password)
            self.user_repository.update_reset_pwd_token(email=user_email, sent_at=0, token="")
        
        elif user_type == "admin":
            self.admin_repository.update_pwd(user_id, new_password)
            self.admin_repository.update_reset_pwd_token(email=user_email, sent_at=0, token="")

    def execute(self, reset_pwd_dto: ResetPwdDTO, response: Response, request: Request):
        token = reset_pwd_dto.token
        new_password = reset_pwd_dto.password

        # 1) Tenta achar o usuário em qualquer repositório
        found_user, user_type = self._find_user_in_any_repo_by_token(token)

        if not found_user:
            response.status_code = 404
            return {
                "status": "error",
                "message": "Não foi possível achar usuário/admin com o token fornecido."
            }

        # 2) Verificar se expirou (exemplo: 900 segundos = 15 min)
        now_ts = datetime.now().timestamp()
        token_ts = found_user.reset_pwd_token_sent_at

        if now_ts - token_ts > 900:  # se se passaram mais de 900s, expirou
            response.status_code = 400
            return {
                "status": "error",
                "message": "O token de redefinição expirou. Por favor, solicite um novo."
            }

        # 3) Atualiza a senha e limpa token
        self._update_password_and_clear_token(
            user_type=user_type,
            user_id=found_user.id,
            user_email=found_user.email,
            new_password=new_password
        )

        return {
            "status": "success",
            "message": "Senha alterada com sucesso. Faça login com sua nova senha."
        }
