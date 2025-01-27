from repositories.finance_repository import FinanceRepository
from fastapi import Request, Response, HTTPException
import os
import jwt

class DeleteFinanceUseCase:
    def __init__(self, finances_repository: FinanceRepository):
        self.finances_repository = finances_repository

    def execute(self, finance_id: str, response: Response, request: Request):
        token = request.cookies.get("user_auth_token")

        payload = jwt.decode(
            token.split(" ")[1],
            os.getenv("USER_JWT_SECRET"),
            algorithms=["HS256"]
        )

        user_id = payload.get("id")
        if not user_id:
            response.status_code = 404
            return {"status": "error", "message": "Usuário não encontrado"}

        deleted = self.finances_repository.delete_finance_by_id(finance_id, user_id)

        if not deleted:  
            response.status_code = 404
            return {"status": "error", "message": "finance não encontrada ou não pertence a este usuário"}

        response.status_code = 200
        return {"status": "success", "message": "finance deletada com sucesso"}
