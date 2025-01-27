from repositories.finance_repository import FinanceRepository
from fastapi import Request, Response
from entities.finance import Finance
import os
import jwt

class GetFinanceUseCase:
    def __init__(self, finances_repository: FinanceRepository):
        self.finances_repository = finances_repository

    def execute(self, response: Response, request: Request):
        token = request.cookies.get("user_auth_token")
        try:
            payload = jwt.decode(token.split(" ")[1], os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])
            user_id = payload.get("id")
        except (jwt.DecodeError, IndexError, AttributeError):
            response.status_code = 401
            return {"status": "error", "message": "Invalid or missing token"}

        if not user_id:
            response.status_code = 404
            return {"status": "error", "message": "Usuário não encontrado"}

        finance = self.finances_repository.get_finance_by_user_id(user_id)
        if finance is None:
            response.status_code = 200
            return []  

        response.status_code = 200
        return finance

    
class GetDespesasUseCase:
    def __init__(self, finances_repository: FinanceRepository):
        self.finances_repository = finances_repository

    def execute(self, response: Response, request: Request):
        token = request.cookies.get("user_auth_token")
        try:
            payload = jwt.decode(token.split(" ")[1], os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])
            user_id = payload.get("id")
        except (jwt.DecodeError, IndexError, AttributeError):
            response.status_code = 401
            return {"status": "error", "message": "Invalid or missing token"}

        if not user_id:
            response.status_code = 404
            return {"status": "error", "message": "Usuário não encontrado"}

        despesas = self.finances_repository.get_despesas_by_user_id(user_id)
        if despesas is None:
            response.status_code = 200
            return []

        response.status_code = 200
        return despesas

    
class GetReceitasUseCase:
    def __init__(self, finances_repository: FinanceRepository):
        self.finances_repository = finances_repository

    def execute(self, response: Response, request: Request):
        token = request.cookies.get("user_auth_token")
        try:
            payload = jwt.decode(token.split(" ")[1], os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])
            user_id = payload.get("id")
        except (jwt.DecodeError, IndexError, AttributeError):
            response.status_code = 401
            return {"status": "error", "message": "Invalid or missing token"}

        if not user_id:
            response.status_code = 404
            return {"status": "error", "message": "Usuário não encontrado"}

        receitas = self.finances_repository.get_receitas_by_user_id(user_id)
        if receitas is None:
            response.status_code = 200
            return []

        response.status_code = 200
        return receitas
