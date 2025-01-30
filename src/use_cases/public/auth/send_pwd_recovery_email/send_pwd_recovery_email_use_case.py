from datetime import datetime
import uuid
from repositories.user_repository import UsersRepository
from repositories.admin_repository import adminsRepository
from utils.send_email import send_email

class SendPwdRecoveryEmailUseCase:
    def __init__(self, user_repository: UsersRepository, admin_repository: adminsRepository):
        self.user_repository = user_repository
        self.admin_repository = admin_repository

    def find_user_in_any_repo(self, email: str):
        user = self.user_repository.find_by_email(email=email)
        if user:
            return (user[0], "user") 
        
        admin = self.admin_repository.find_by_email(email=email)
        if admin:
            return (admin[0], "admin") 

        return (None, None)
    
    def update_user_in_repo(self, user_type: str, email: str, sent_at: float, token: str):
        if user_type == "user":
            self.user_repository.update_reset_pwd_token(
                email=email,
                sent_at=sent_at,
                token=token
            )
        elif user_type == "admin":
            self.admin_repository.update_reset_pwd_token(
                email=email,
                sent_at=sent_at,
                token=token
            )

    def execute(self, send_pwd_recovery_email_dto, response, request):
        email = send_pwd_recovery_email_dto.email
        
        # 1) Tenta achar em qualquer repositório
        found_user, user_type = self.find_user_in_any_repo(email)

        if not found_user:
            response.status_code = 404
            return {
                "status": "error",
                "message": "Não foi possível achar nenhum usuário com o email fornecido"
            }
        
        # 2) Verifica se o token foi enviado há menos de 1h
        # if found_user.reset_pwd_token_sent_at + 3600 > datetime.now().timestamp():
        #     response.status_code = 400
        #     return {
        #         "status": "error", 
        #         "message": "Você pode solicitar o link para redefinir sua senha a cada 1 hora."
        #     }
        
        # 3) Gera token e atualiza no repositório correto
        token = str(uuid.uuid4())
        self.update_user_in_repo(
            user_type,
            email=found_user.email,
            sent_at=datetime.now().timestamp(),
            token=token
        )

        # 4) Envia e-mail
        reset_url = f"http://localhost:5173/auth/reset-password/{token}"
        email_content = f"""
            <p>Redefina sua senha clicando no link abaixo:</p>
            <a href="{reset_url}">{reset_url}</a>
        """
        
        send_email(
            email=found_user.email,
            content=email_content
        )

        response.status_code = 200
        return {
            "status": "success",
            "message": "Link de redefinição de senha enviado com sucesso"
        }
