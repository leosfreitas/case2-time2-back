from fastapi import Request, Response, APIRouter, Depends
from repositories.pacote_repository import PacoteRepository
from .create_pacote_dto import CreatePacoteDTO
from .create_pacote_use_case import CreatePacoteUseCase
from middlewares.validate_user_auth_token import validade_user_auth_token

router = APIRouter()
create_pacote_use_case = CreatePacoteUseCase(PacoteRepository())

@router.post("/pacote/create")
def create_pacote(
    create_pacote_dto: CreatePacoteDTO,
    response: Response,
    request: Request,
):
    return create_pacote_use_case.execute(create_pacote_dto, response, request)
