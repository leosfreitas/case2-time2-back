from fastapi import APIRouter, Request, Response, Depends
from use_cases.admin.pacote.edit_pacote.edit_pacote_use_case import EditPacoteUseCase
from repositories.pacote_repository import PacoteRepository
from .edit_pacote_dto import EditPacoteDTO
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()

pacote_repository = PacoteRepository()
edit_pacote_use_case = EditPacoteUseCase(pacote_repository)

@router.put("/pacote/edit/{pacote_id}", dependencies=[Depends(validade_admin_auth_token)])
def edit_pacote(pacote_id: str, edit_pacote_dto: EditPacoteDTO, response: Response, request: Request):
    return edit_pacote_use_case.execute(pacote_id, edit_pacote_dto, response, request)
