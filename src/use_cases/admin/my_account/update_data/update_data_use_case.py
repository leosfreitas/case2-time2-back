from repositories.user_repository import UsersRepository
from use_cases.user.my_account.update_data.update_data_dto import UpdateDataDTO
from fastapi import Request, Response

class UpdateDataUseCase:
    user_repository = UsersRepository

    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    def execute(self, update_data_dto: UpdateDataDTO, response: Response, request: Request):
        user_id = request.state.auth_payload["user_id"]
        if not update_data_dto.name or not update_data_dto.email:
            response.status_code = 406
            return{"status": "error", "message": "Alteração não realizada, pois falta informações"}

        self.user_repository.update_name(user_id, update_data_dto.name)
        self.user_repository.update_email(user_id, update_data_dto.email)
        self.user_repository.update_cpf(user_id, update_data_dto.cpf)
        self.user_repository.update_phone(user_id, update_data_dto.phone)

        response.status_code = 202
        return{"status": "success", "message": "Atualização do cadastro realizado com sucesso"}