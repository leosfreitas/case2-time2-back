from fastapi import Request, Response
from repositories.acordo_repository import AcordoRepository

class DeleteAcordoUseCase:
    def __init__(self, acordo_repository: AcordoRepository):
        self.acordo_repository = acordo_repository

    def execute(self, acordo_id: str, response: Response, request: Request):
        deleted = self.acordo_repository.delete_acordo_by_id(acordo_id)
        if not deleted:
            response.status_code = 404
            return {
                "status": "error",
                "message": f"Acordo com ID {acordo_id} não encontrado."
            }
        response.status_code = 200
        return {
            "status": "success",
            "message": f"Acordo com ID {acordo_id} deletado com sucesso."
        }
