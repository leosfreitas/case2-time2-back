from fastapi import APIRouter, Request, Response, Depends
from middlewares.validate_user_auth_token import validade_user_auth_token
from repositories.budget_repository import BudgetRepository
from use_cases.user.budget.create_budget.create_budget_dto import CreateBudgetDTO
from use_cases.user.budget.create_budget.create_budget_use_case import CreateBudgetUseCase

router = APIRouter()

create_budget_use_case = CreateBudgetUseCase(BudgetRepository())

@router.post("/user/create-budget", dependencies=[Depends(validade_user_auth_token)])
def create_budget(create_budget_dto: CreateBudgetDTO, response: Response, request: Request):
    return create_budget_use_case.execute(create_budget_dto, response, request)
