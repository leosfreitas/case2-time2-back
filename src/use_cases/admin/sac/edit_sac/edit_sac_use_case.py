from repositories.sac_repository import SacRepository
from .edit_sac_dto import EditSacDTO
from fastapi import Request, Response
from bson import ObjectId

class EditSacUseCase:
    def __init__(self, sac_repository: SacRepository):
        self.sac_repository = sac_repository

    def execute(self, sac_id: str, edit_sac_dto: EditSacDTO, response: Response, request: Request):
        # Valida se o sac_id é um ObjectId válido do MongoDB
        if not ObjectId.is_valid(sac_id):
            response.status_code = 400
            return {"status": "error", "message": "ID de SAC inválido."}

        # Atualiza apenas o campo resposta
        sac_atualizado = self.sac_repository.update_sac_resposta(
            sac_id=sac_id,
            resposta=edit_sac_dto.resposta
        )

        if not sac_atualizado:
            response.status_code = 404
            return {"status": "error", "message": f"SAC com ID {sac_id} não encontrado."}

        response.status_code = 202
        return {"status": "success", "message": "Resposta do SAC atualizada com sucesso."}
