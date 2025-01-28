from use_cases.admin.my_account.get_data.get_data_use_case import getAdminData
from repositories.admin_repository import adminsRepository
from middlewares.validate_admin_auth_token import validade_admin_auth_token
from fastapi import APIRouter, Request, Response, Depends

router = APIRouter()

admin_repository = adminsRepository()

get_data_use_case = getAdminData(admin_repository)

@router.get("/admin/data", dependencies=[Depends(validade_admin_auth_token)])
def get_user_data(response: Response, request:Request):
    return get_data_use_case.execute(response,request)