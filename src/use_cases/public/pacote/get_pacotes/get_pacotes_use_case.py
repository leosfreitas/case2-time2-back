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
