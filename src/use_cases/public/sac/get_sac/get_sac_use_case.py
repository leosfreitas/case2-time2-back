from repositories.sac_repository import SacRepository
from fastapi import Response

class GetAllSacsUseCase:
    def __init__(self, sac_repository: SacRepository):
        self.sac_repository = sac_repository

    def execute(self, response: Response):
        sacs = self.sac_repository.get_all_sacs()

        if not sacs:
            response.status_code = 404
            return {"status": "error", "message": "Nenhum SAC encontrado."}

        response.status_code = 200
        return {"status": "success", "data": sacs}
