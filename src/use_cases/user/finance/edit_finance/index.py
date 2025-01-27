from repositories.finance_repository import FinanceRepository
from fastapi import APIRouter, Request, Response, Depends
from use_cases.user.finance.edit_finance.edit_finance_use_case import EditFinanceUseCase
from .edit_finance_dto import EditFinanceDTO
from middlewares.validate_user_auth_token import validade_user_auth_token

router = APIRouter()

finances_repository = FinanceRepository()
edit_finance_use_case = EditFinanceUseCase(finances_repository)

@router.put("/user/edit-finance/{finance_id}", dependencies=[Depends(validade_user_auth_token)])
def edit_finance(finance_id: str, edit_finance_dto: EditFinanceDTO, response: Response, request: Request):
    return edit_finance_use_case.execute(finance_id, edit_finance_dto, response, request)
