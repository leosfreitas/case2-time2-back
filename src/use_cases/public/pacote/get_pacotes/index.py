from fastapi import APIRouter, Request, Response, Depends
from .get_pacotes_use_case import GetPacotesUseCase, GetPacoteUseCase
from repositories.pacote_repository import PacoteRepository

router = APIRouter()

get_pacotes_use_case = GetPacotesUseCase(PacoteRepository())

get_pacote_use_case = GetPacoteUseCase(PacoteRepository())

@router.get("/pacotes/get")
def get_pacotes(response: Response, request: Request):
    return get_pacotes_use_case.execute(response, request)

@router.get("/pacote/get/{pacote_id}")
def get_pacote(response: Response, request: Request, pacote_id: str):
    return get_pacote_use_case.execute(response, request, pacote_id)