from fastapi import APIRouter, Request, Response, Depends
from repositories.acordo_repository import AcordoRepository
from .get_acordo_use_case import GetAllAcordosUseCase
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()

acordo_repository = AcordoRepository()
get_all_acordos_use_case = GetAllAcordosUseCase(acordo_repository)

@router.get("/admin/acordo/get", dependencies=[Depends(validade_admin_auth_token)])
def get_all_acordos(response: Response, request: Request):
    return get_all_acordos_use_case.execute(response, request)
