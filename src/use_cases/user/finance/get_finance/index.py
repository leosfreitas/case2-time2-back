from repositories.finance_repository import FinanceRepository
from .get_finance_use_case import GetFinanceUseCase, GetDespesasUseCase, GetReceitasUseCase
from fastapi import Request, Response, APIRouter, Depends
from middlewares.validate_user_auth_token import validade_user_auth_token

router = APIRouter()

get_finances_use_case = GetFinanceUseCase(FinanceRepository())

get_despesas_use_case = GetDespesasUseCase(FinanceRepository())

get_receitas_use_case = GetReceitasUseCase(FinanceRepository())

@router.get("/user/get-finances", dependencies=[Depends(validade_user_auth_token)])
def get_finances(response:Response, request:Request):
    return get_finances_use_case.execute(response, request)

@router.get("/user/get-despesas", dependencies=[Depends(validade_user_auth_token)])
def get_despesas(response:Response, request:Request):
    return get_despesas_use_case.execute(response, request)

@router.get("/user/get-receitas", dependencies=[Depends(validade_user_auth_token)])
def get_receitas(response:Response, request:Request):
    return get_receitas_use_case.execute(response, request)