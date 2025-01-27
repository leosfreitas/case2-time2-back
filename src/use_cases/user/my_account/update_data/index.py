from repositories.user_repository import UsersRepository
from fastapi import FastAPI, Request, Response
from .update_data_use_case import UpdateDataUseCase
from .update_data_dto import UpdateDataDTO
from fastapi import APIRouter, Request, Response, Depends
from middlewares.validate_user_auth_token import validade_user_auth_token

router = APIRouter()

user_repository = UsersRepository()
update_data_use_case = UpdateDataUseCase(user_repository)

@router.put("/user/update/data", dependencies=[Depends(validade_user_auth_token)])
def updata_data(update_data_dto: UpdateDataDTO, response: Response, request: Request):
    return update_data_use_case.execute(update_data_dto, response, request)
