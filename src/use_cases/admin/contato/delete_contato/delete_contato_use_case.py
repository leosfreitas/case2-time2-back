from fastapi import Request, Response
from repositories.contato_repository import ContatoRepository

class DeleteContatoUseCase:
    def __init__(self, contato_repository: ContatoRepository):
        self.contato_repository = contato_repository

    def execute(self, contato_id: str, response: Response, request: Request):
        contato_deleted = self.contato_repository.delete_contato_by_id(contato_id)
        if not contato_deleted:
            response.status_code = 404
            return {
                "status": "error",
                "message": f"Contato com ID {contato_id} não encontrado."
            }

        response.status_code = 200
        return {
            "status": "success",
            "message": f"Contato com ID {contato_id} deletado com sucesso."
        }
