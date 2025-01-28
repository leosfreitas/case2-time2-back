from use_cases.admin.headbar.get_user_name_use_case import getUserName
from repositories.admin_repository import adminsRepository
from middlewares.validate_admin_auth_token import validade_admin_auth_token
from fastapi import APIRouter, Request, Response, Depends

router = APIRouter()

admin_repository = adminsRepository()

get_user_name_use_case = getUserName(admin_repository)

@router.get("/admin/headbar", dependencies=[Depends(validade_admin_auth_token)])
def get_user_name(response: Response, request:Request):
    return get_user_name_use_case.execute(response,request)