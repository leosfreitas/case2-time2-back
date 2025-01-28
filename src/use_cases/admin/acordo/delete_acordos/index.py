from fastapi import APIRouter, Request, Response, Depends
from .detete_acordo_use_case import DeleteAcordoUseCase
from repositories.acordo_repository import AcordoRepository
from middlewares.validate_admin_auth_token import validade_admin_auth_token


router = APIRouter()

acordo_repository = AcordoRepository()
delete_acordo_use_case = DeleteAcordoUseCase(acordo_repository)

@router.delete("/admin/acordo/delete/{acordo_id}", dependencies=[Depends(validade_admin_auth_token)])
def delete_acordo(acordo_id: str, response: Response, request: Request):
    return delete_acordo_use_case.execute(acordo_id, response, request)