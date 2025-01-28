from fastapi import APIRouter, Request, Response, Depends
from .create_acordo_use_case import CreateAcordoUseCase
from .create_acordo_dto import CreateAcordoDTO
from repositories.acordo_repository import AcordoRepository
from middlewares.validate_user_auth_token import validade_user_auth_token

router = APIRouter()

acordo_repository = AcordoRepository()
create_acordo_use_case = CreateAcordoUseCase(acordo_repository)

@router.post("/user/acordo/create", dependencies=[Depends(validade_user_auth_token)])
def create_acordo(dto: CreateAcordoDTO, response: Response, request: Request):
    return create_acordo_use_case.execute(dto, response, request)
