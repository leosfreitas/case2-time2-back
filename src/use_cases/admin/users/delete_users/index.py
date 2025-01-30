from fastapi import APIRouter, Request, Response, Depends
from .delete_user_use_case import DeleteUserUseCase
from repositories.user_repository import UsersRepository
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()

delete_user_use_case = DeleteUserUseCase(UsersRepository())

@router.delete("/user/delete/{user_id}", dependencies=[Depends(validade_admin_auth_token)])
def delete_user(user_id: str, response: Response, request: Request):
    return delete_user_use_case.execute(user_id, response, request)

