from fastapi import Request, Response
from repositories.pacote_repository import PacoteRepository

class GetPacotesUseCase:
    def __init__(self, pacote_repository: PacoteRepository):
        self.pacote_repository = pacote_repository

    def execute(self, response: Response, request: Request):
        pacotes = self.pacote_repository.get_all_pacotes()

        if not pacotes:
            response.status_code = 200
            return []

        response.status_code = 200
        return pacotes

class GetPacoteUseCase: 
    def __init__(self, pacote_repository: PacoteRepository):
        self.pacote_repository = pacote_repository

    def execute(self, response: Response, request: Request, pacote_id: str):
        pacote = self.pacote_repository.get_pacote_by_id(pacote_id)

        if not pacote:
            response.status_code = 404
            return {"message": "Pacote não encontrado"}

        response.status_code = 200
        return pacote