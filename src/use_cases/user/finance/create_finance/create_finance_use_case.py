from use_cases.user.finance.create_finance.create_finance_dto import CreateFinanceDTO
from fastapi import Request, Response, HTTPException
from repositories.finance_repository import FinanceRepository
from entities.finance import Finance
import jwt
import os

class CreatefinanceUseCase:
    def __init__(self, finance_repository: FinanceRepository):
        self.finance_repository = finance_repository

    def execute(self, create_finance_dto: CreateFinanceDTO, response: Response, request: Request):
        token = request.cookies.get("user_auth_token")

        payload = jwt.decode(token.split(" ")[1], os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])

        user_id = payload.get("id")
        user_email = payload.get("email")
        request.state.auth_payload = {"user_id": user_id, "user_email": user_email}

        if not user_id:
            response.status_code = 407
            return {"status": "error", "message":"Usuário não encontrado"}

        finance = Finance(
            user=user_id,
            categoria=create_finance_dto.categoria,
            tipo=create_finance_dto.tipo,
            valor=create_finance_dto.valor,
            data=create_finance_dto.data,
            descricao=create_finance_dto.descricao
        )

        self.finance_repository.save(finance)
        response.status_code=200
        return {"status": "success", "message":"finance criada"}
