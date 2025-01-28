from repositories.pacote_repository import PacoteRepository
from .edit_pacote_dto import EditPacoteDTO
from fastapi import Request, Response
from bson import ObjectId

class EditPacoteUseCase:
    def __init__(self, pacote_repository: PacoteRepository):
        self.pacote_repository = pacote_repository

    def execute(self, pacote_id: str, edit_pacote_dto: EditPacoteDTO, response: Response, request: Request):
        if not ObjectId.is_valid(pacote_id):
            response.status_code = 400
            return {"status": "error", "message": "ID de pacote inválido."}

        if not any([edit_pacote_dto.tipo, edit_pacote_dto.preco, edit_pacote_dto.cortesia, edit_pacote_dto.nome, edit_pacote_dto.detalhes]):
            response.status_code = 406
            return {"status": "error", "message": "Nenhuma informação enviada para editar o pacote."}

        pacote_atualizado = self.pacote_repository.update_pacote(
            pacote_id=pacote_id,
            tipo=edit_pacote_dto.tipo,
            preco=edit_pacote_dto.preco,
            cortesia=edit_pacote_dto.cortesia,
            nome=edit_pacote_dto.nome,
            detalhes=edit_pacote_dto.detalhes,
        )

        if not pacote_atualizado:
            response.status_code = 404
            return {"status": "error", "message": f"Pacote com ID {pacote_id} não encontrado."}

        response.status_code = 202
        return {"status": "success", "message": "Pacote atualizado com sucesso."}
