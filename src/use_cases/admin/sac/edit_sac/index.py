from fastapi import APIRouter, Request, Response, Depends
from .edit_sac_use_case import EditSacUseCase
from .edit_sac_dto import EditSacDTO
from repositories.sac_repository import SacRepository
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()

sac_repository = SacRepository()
edit_sac_use_case = EditSacUseCase(sac_repository)

@router.put("/sac/edit/{sac_id}", dependencies=[Depends(validade_admin_auth_token)])
def update_sac_resposta(sac_id: str, edit_sac_dto: EditSacDTO, response: Response, request: Request):
    return edit_sac_use_case.execute(sac_id, edit_sac_dto, response, request)
