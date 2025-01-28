from fastapi import APIRouter, Request, Response, Depends
from .delete_sac_use_case import DeleteSacUseCase
from repositories.sac_repository import SacRepository
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()

delete_sac_use_case = DeleteSacUseCase(SacRepository())

@router.delete("/sac/delete/{sac_id}", dependencies=[Depends(validade_admin_auth_token)])
def delete_sac(sac_id: str, response: Response, request: Request):
    return delete_sac_use_case.execute(sac_id, response, request)
