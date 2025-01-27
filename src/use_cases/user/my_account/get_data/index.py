from use_cases.user.my_account.get_data.get_data_use_case import getUserData
from repositories.user_repository import UsersRepository
from middlewares.validate_user_auth_token import validade_user_auth_token
from fastapi import APIRouter, Request, Response, Depends

router = APIRouter()

user_repository = UsersRepository()

get_data_use_case = getUserData(user_repository)

@router.get("/user/data", dependencies=[Depends(validade_user_auth_token)])
def get_user_data(response: Response, request:Request):
    return get_data_use_case.execute(response,request)