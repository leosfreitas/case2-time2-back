from fastapi import Request, Response
from bson import ObjectId
from .edit_contato_dto import EditContatoDTO
from repositories.contato_repository import ContatoRepository

class EditContatoUseCase:
    def __init__(self, contato_repository: ContatoRepository):
        self.contato_repository = contato_repository

    def execute(self, contato_id: str, edit_contato_dto: EditContatoDTO, response: Response, request: Request):
        if not ObjectId.is_valid(contato_id):
            response.status_code = 400
            return {"status": "error", "message": "ID de contato inválido."}

        if not any([
            edit_contato_dto.mensagem,
        ]):
            response.status_code = 406
            return {"status": "error", "message": "Nenhuma informação enviada para editar o contato."}

        atualizado = self.contato_repository.update_contato(
            mensagem=edit_contato_dto.mensagem,
        )

        if not atualizado:
            response.status_code = 404
            return {"status": "error", "message": f"Contato com ID {contato_id} não encontrado."}

        response.status_code = 202
        return {"status": "success", "message": "Contato atualizado com sucesso."}
