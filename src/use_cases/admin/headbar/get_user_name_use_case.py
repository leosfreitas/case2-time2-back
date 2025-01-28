from repositories.admin_repository import adminsRepository
from fastapi import Request, Response

class getUserName:
    def __init__(self, admin_repository: adminsRepository) -> None:
        self.admin_repository = admin_repository

    def execute(self, response: Response, request:Request):
        admin_id = request.state.auth_payload["admin_id"]
        user_name = self.admin_repository.get_name(admin_id)

        return {"status":"success", "user_name":user_name}