from repositories.admin_repository import adminsRepository
from fastapi import FastAPI, Request, Response
from .update_data_use_case import UpdateDataUseCase
from .update_data_dto import UpdateDataDTO
from fastapi import APIRouter, Request, Response, Depends
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()

admin_repository = adminsRepository()
update_data_use_case = UpdateDataUseCase(admin_repository)

@router.put("/admin/update/data", dependencies=[Depends(validade_admin_auth_token)])
def updata_data(update_data_dto: UpdateDataDTO, response: Response, request: Request):
    return update_data_use_case.execute(update_data_dto, response, request)
