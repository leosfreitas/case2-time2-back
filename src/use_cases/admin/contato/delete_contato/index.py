from fastapi import APIRouter, Request, Response, Depends
from .delete_contato_use_case import DeleteContatoUseCase
from repositories.contato_repository import ContatoRepository
from middlewares.validate_user_auth_token import validade_user_auth_token

router = APIRouter()

contato_repository = ContatoRepository()
delete_contato_use_case = DeleteContatoUseCase(contato_repository)

@router.delete("/contato/delete/{contato_id}", dependencies=[Depends(validade_user_auth_token)])
def delete_contato(contato_id: str, response: Response, request: Request):
    return delete_contato_use_case.execute(contato_id, response, request)
