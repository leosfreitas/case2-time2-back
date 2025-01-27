from fastapi import APIRouter, Request, Response, Depends
from middlewares.validate_user_auth_token import validade_user_auth_token
from repositories.budget_repository import BudgetRepository
from use_cases.user.budget.delete_budget.delete_budget_use_case import DeleteBudgetUseCase

router = APIRouter()

delete_budget_use_case = DeleteBudgetUseCase(BudgetRepository())

@router.delete("/user/delete-budget/{budget_id}", dependencies=[Depends(validade_user_auth_token)])
def delete_budget(budget_id: str, response: Response, request: Request):
    return delete_budget_use_case.execute(budget_id, response, request)
