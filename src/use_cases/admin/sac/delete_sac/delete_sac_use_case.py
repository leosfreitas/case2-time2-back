import os
import jwt
from fastapi import Request, Response
from repositories.sac_repository import SacRepository

class DeleteSacUseCase:
    def __init__(self, sac_repository: SacRepository):
        self.sac_repository = sac_repository

    def execute(self, sac_id: str, response: Response, request: Request):
        sac_deleted = self.sac_repository.delete_sac_by_id(sac_id)
    
        if not sac_deleted:
            response.status_code = 404
            return {"status": "error", "message": f"SAC com ID {sac_id} não encontrado"}

        response.status_code = 200
        return {"status": "success", "message": f"SAC com ID {sac_id} deletado com sucesso"}
