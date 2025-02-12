from fastapi import Request, Response, APIRouter, Depends
from repositories.pacote_repository import PacoteRepository
from .create_pacote_dto import CreatePacoteDTO
from .create_pacote_use_case import CreatePacoteUseCase
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()
create_pacote_use_case = CreatePacoteUseCase(PacoteRepository())

@router.post("/pacote/create", dependencies=[Depends(validade_admin_auth_token)])
def create_pacote(
    create_pacote_dto: CreatePacoteDTO,
    response: Response,
    request: Request,
):
    return create_pacote_use_case.execute(create_pacote_dto, response, request)
