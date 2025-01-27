from repositories.budget_repository import BudgetRepository
from fastapi import Request, Response
import jwt, os

class DeleteBudgetUseCase:
    def __init__(self, budget_repository: BudgetRepository):
        self.budget_repository = budget_repository

    def execute(self, budget_id: str, response: Response, request: Request):
        token = request.cookies.get("user_auth_token")
        payload = jwt.decode(token.split(" ")[1], os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])
        user_id = payload.get("id")
        if not user_id:
            response.status_code = 404
            return {"status": "error", "message": "Usuário não encontrado"}

        deleted = self.budget_repository.delete_budget_by_id(budget_id, user_id)
        if not deleted:
            response.status_code = 404
            return {"status": "error", "message": "Budget não encontrada ou não pertence a este usuário"}

        response.status_code = 200
        return {"status": "success", "message": "Budget deletada com sucesso"}
