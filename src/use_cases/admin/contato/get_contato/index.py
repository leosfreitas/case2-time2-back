from fastapi import APIRouter, Request, Response, Depends
from repositories.contato_repository import ContatoRepository
from .get_contato_use_case import GetAllContatosUseCase
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()

contato_repository = ContatoRepository()
get_all_contatos_use_case = GetAllContatosUseCase(contato_repository)

@router.get("/admin/contatos/get", dependencies=[Depends(validade_admin_auth_token)])
def get_all_contatos(response: Response, request: Request):
    return get_all_contatos_use_case.execute(response, request)
