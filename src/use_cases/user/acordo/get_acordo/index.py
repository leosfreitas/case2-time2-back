# use_cases/acordo/get_acordos_by_logged_user/index.py

from fastapi import APIRouter, Request, Response, Depends
from .get_acordo_use_case import GetAcordosByLoggedUserUseCase
from repositories.acordo_repository import AcordoRepository
from middlewares.validate_user_auth_token import validade_user_auth_token

router = APIRouter()

acordo_repository = AcordoRepository()
get_acordos_by_logged_user_use_case = GetAcordosByLoggedUserUseCase(acordo_repository)

@router.get("/user/acordo/get", dependencies=[Depends(validade_user_auth_token)])
def get_my_acordos(response: Response, request: Request):
    return get_acordos_by_logged_user_use_case.execute(response, request)
