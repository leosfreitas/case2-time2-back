from fastapi import APIRouter, Request, Response, Depends
from .delete_pacote_use_case import DeletePacoteUseCase
from repositories.pacote_repository import PacoteRepository
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()

delete_pacote_use_case = DeletePacoteUseCase(PacoteRepository())

@router.delete("/pacote/delete/{pacote_id}", dependencies=[Depends(validade_admin_auth_token)])
def delete_pacote(pacote_id: str, response: Response, request: Request):
    return delete_pacote_use_case.execute(pacote_id, response, request)
