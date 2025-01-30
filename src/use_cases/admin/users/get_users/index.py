from fastapi import APIRouter, Response, Depends
from use_cases.admin.users.get_users.get_users_use_case import GetUsersUseCase
from repositories.user_repository import UsersRepository
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()

user_repository = UsersRepository()
get_users_use_case = GetUsersUseCase(user_repository)

@router.get("/users/get", dependencies=[Depends(validade_admin_auth_token)])
def get_users(response: Response):
    return get_users_use_case.execute(response)
