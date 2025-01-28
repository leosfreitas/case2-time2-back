from repositories.contato_repository import ContatoRepository
from .get_contato_use_case import GetContatoUseCase
from fastapi import Request, Response, APIRouter, Depends
from middlewares.validate_user_auth_token import validade_user_auth_token

router = APIRouter()

get_contato_use_case = GetContatoUseCase(ContatoRepository())

@router.get("/user/contato/get", dependencies=[Depends(validade_user_auth_token)])
def get_finances(response:Response, request:Request):
    return get_contato_use_case.execute(response, request)