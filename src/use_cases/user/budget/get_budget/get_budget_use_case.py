from repositories.budget_repository import BudgetRepository
from fastapi import Request, Response
import jwt, os

class GetBudgetsUseCase:
    def __init__(self, budget_repository: BudgetRepository):
        self.budget_repository = budget_repository

    def execute(self, response: Response, request: Request):
        token = request.cookies.get("user_auth_token")
        try:
            payload = jwt.decode(token.split(" ")[1], os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])
        except Exception:
            response.status_code = 401
            return {"status": "error", "message": "Token inválido"}

        user_id = payload.get("id")
        if not user_id:
            response.status_code = 404
            return {"status": "error", "message": "Usuário não encontrado"}

        budgets = self.budget_repository.get_budgets_by_user_id(user_id)
        response.status_code = 200
        return budgets
