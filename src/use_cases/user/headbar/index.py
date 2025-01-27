from use_cases.user.headbar.get_user_name_use_case import getUserName
from repositories.user_repository import UsersRepository
from middlewares.validate_user_auth_token import validade_user_auth_token
from fastapi import APIRouter, Request, Response, Depends

router = APIRouter()

user_repository = UsersRepository()

get_user_name_use_case = getUserName(user_repository)

@router.get("/user/headbar", dependencies=[Depends(validade_user_auth_token)])
def get_user_name(response: Response, request:Request):
    return get_user_name_use_case.execute(response,request)