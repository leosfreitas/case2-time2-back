from fastapi import APIRouter, Request, Response, Depends
from middlewares.validate_user_auth_token import validade_user_auth_token
from repositories.budget_repository import BudgetRepository
from use_cases.user.budget.get_budget.get_budget_use_case import GetBudgetsUseCase

router = APIRouter()

get_budgets_use_case = GetBudgetsUseCase(BudgetRepository())

@router.get("/user/get-budgets", dependencies=[Depends(validade_user_auth_token)])
def get_budgets(response: Response, request: Request):
    return get_budgets_use_case.execute(response, request)
