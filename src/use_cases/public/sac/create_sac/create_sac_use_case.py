from use_cases.public.sac.create_sac.create_sac_dto import CreateSacDTO
from fastapi import Request, Response, HTTPException
from repositories.sac_repository import SacRepository
from entities.sac import Sac
import jwt
import os

class CreateSacUseCase:
    def __init__(self, sac_respository: SacRepository):
        self.sac_respository = sac_respository

    def execute(self, create_sac_dto: CreateSacDTO, response: Response, request: Request):

        sac = Sac(
            nome=create_sac_dto.nome,
            email=create_sac_dto.email,
            motivo=create_sac_dto.motivo,
            mensagem=create_sac_dto.mensagem
        )

        self.sac_respository.save(sac)
        response.status_code=200
        return {"status": "success", "message":"Sac criado com sucesso"}
