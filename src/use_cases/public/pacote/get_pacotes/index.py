from fastapi import APIRouter, Request, Response, Depends
from .get_pacotes_use_case import GetPacotesUseCase
from repositories.pacote_repository import PacoteRepository

router = APIRouter()

get_pacotes_use_case = GetPacotesUseCase(PacoteRepository())

@router.get("/pacotes/get")
def get_pacotes(response: Response, request: Request):
    return get_pacotes_use_case.execute(response, request)
