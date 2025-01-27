from repositories.finance_repository import FinanceRepository
from .delete_finance_use_case import DeleteFinanceUseCase
from fastapi import Request, Response, APIRouter, Depends
from middlewares.validate_user_auth_token import validade_user_auth_token

router = APIRouter()

delete_finance_use_case = DeleteFinanceUseCase(FinanceRepository())

@router.delete("/user/delete-finance/{finance_id}",  dependencies=[Depends(validade_user_auth_token)])
def delete_finance(finance_id: str, response: Response, request: Request):
    return delete_finance_use_case.execute(finance_id, response, request)