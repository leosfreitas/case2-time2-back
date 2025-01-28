from repositories.admin_repository import adminsRepository
from fastapi import Request, Response

class getAdminData:
    def __init__(self, admin_repository: adminsRepository) -> None:
        self.admin_repository = admin_repository

    def execute(self, response: Response, request: Request):
        admin_id = request.state.auth_payload["admin_id"]
        admin_name = self.admin_repository.get_name(admin_id)
        admin_email = self.admin_repository.get_email(admin_id)
        admin_cpf = self.admin_repository.get_cpf(admin_id)
        admin_phone = self.admin_repository.get_phone(admin_id)

        return {"status":"success", "data": {"name": admin_name, 
                                             "email": admin_email, 
                                             "cpf": admin_cpf,
                                             "phone": admin_phone,
                                             "id": admin_id}}