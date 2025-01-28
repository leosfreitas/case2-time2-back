from fastapi import APIRouter, Request, Response, Depends
from .create_contato_use_case import CreateContatoUseCase
from .create_contato_dto import CreateContatoDTO
from repositories.contato_repository import ContatoRepository
from middlewares.validate_user_auth_token import validade_user_auth_token

router = APIRouter()

contato_repository = ContatoRepository()
create_contato_use_case = CreateContatoUseCase(contato_repository)

@router.post("/user/contato/create", dependencies=[Depends(validade_user_auth_token)])
def create_contato(dto: CreateContatoDTO, response: Response, request: Request):
    return create_contato_use_case.execute(dto, response, request)
