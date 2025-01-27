from use_cases.user.budget.create_budget.create_budget_dto import CreateBudgetDTO
from fastapi import Request, Response
from repositories.budget_repository import BudgetRepository
from entities.budget import Budget
import jwt, os

class CreateBudgetUseCase:
    def __init__(self, budget_repository: BudgetRepository):
        self.budget_repository = budget_repository

    def execute(self, create_budget_dto: CreateBudgetDTO, response: Response, request: Request):
        token = request.cookies.get("user_auth_token")
        payload = jwt.decode(token.split(" ")[1], os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])
        user_id = payload.get("id")
        if not user_id:
            response.status_code = 407
            return {"status": "error", "message": "Usuário não encontrado"}

        budget = Budget(
            _id="",
            user=user_id,
            tipo=create_budget_dto.tipo,
            valor=create_budget_dto.valor
        )

        self.budget_repository.save(budget)
        response.status_code = 200
        return {"status": "success", "message": "Budget criada"}
