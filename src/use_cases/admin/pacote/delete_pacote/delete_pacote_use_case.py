import os
import jwt
from fastapi import Request, Response
from repositories.pacote_repository import PacoteRepository

class DeletePacoteUseCase:
    def __init__(self, pacote_repository: PacoteRepository):
        self.pacote_repository = pacote_repository

    def execute(self, pacote_id: str, response: Response, request: Request):
        
        pacote_deleted = self.pacote_repository.delete_pacote_by_id(pacote_id)
        if not pacote_deleted:
            response.status_code = 404
            return {"status": "error", "message": f"Pacote com ID {pacote_id} não encontrado"}

        response.status_code = 200
        return {"status": "success", "message": f"Pacote com ID {pacote_id} deletado com sucesso"}
