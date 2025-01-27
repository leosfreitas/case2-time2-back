from repositories.finance_repository import FinanceRepository
from .create_finance_dto import CreateFinanceDTO
from .create_finance_use_case import CreatefinanceUseCase   
from fastapi import Request, Response, APIRouter, Depends
from middlewares.validate_user_auth_token import validade_user_auth_token

router = APIRouter()

create_finance_use_case = CreatefinanceUseCase(FinanceRepository())

@router.post("/user/create-finance", dependencies=[Depends(validade_user_auth_token)])
def create_finance(create_finance_dto:CreateFinanceDTO, response:Response, request:Request):
    return create_finance_use_case.execute(create_finance_dto, response, request)