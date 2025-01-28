from fastapi import APIRouter, Request, Response, Depends
from .edit_contato_use_case import EditContatoUseCase
from .edit_contato_dto import EditContatoDTO
from repositories.contato_repository import ContatoRepository
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()

contato_repository = ContatoRepository()
edit_contato_use_case = EditContatoUseCase(contato_repository)

@router.put("/contato/{contato_id}", dependencies=[Depends(validade_admin_auth_token)])
def edit_contato(contato_id: str, dto: EditContatoDTO, response: Response, request: Request):
    return edit_contato_use_case.execute(contato_id, dto, response, request)
