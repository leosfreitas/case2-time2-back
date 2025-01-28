from repositories.acordo_repository import AcordoRepository
from fastapi import Request, Response

class GetAllAcordosUseCase:
    def __init__(self, acordo_repository: AcordoRepository):
        self.acordo_repository = acordo_repository

    def execute(self, response: Response, request: Request):
        all_acordos = self.acordo_repository.get_all_acordos()

        acordos_por_usuario = {}
        for acordo in all_acordos:
            user_id = acordo["user_id"]
            if user_id not in acordos_por_usuario:
                acordos_por_usuario[user_id] = []
            acordos_por_usuario[user_id].append(acordo)

        response.status_code = 200
        return acordos_por_usuario
