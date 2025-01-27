from repositories.finance_repository import FinanceRepository
from .edit_finance_dto import EditFinanceDTO
from fastapi import Request, Response
from bson import ObjectId

class EditFinanceUseCase:
    def __init__(self, finance_repository: FinanceRepository):
        self.finance_repository = finance_repository

    def execute(self, finance_id: str, edit_finance_dto: EditFinanceDTO, response: Response, request: Request):
        if not ObjectId.is_valid(finance_id):
            response.status_code = 400
            return {"status": "error", "message": "ID de finance inválido."}

        if not edit_finance_dto.tipo or not edit_finance_dto.valor:
            response.status_code = 406
            return {"status": "error", "message": "Falta informações obrigatórias para editar a finance."}

        self.finance_repository.update_finance(
            finance_id=finance_id,
            tipo=edit_finance_dto.tipo,
            valor=edit_finance_dto.valor,
            data=edit_finance_dto.data,
            descricao=edit_finance_dto.descricao
        )

        response.status_code = 202
        return {"status": "success", "message": "finance atualizada com sucesso."}
