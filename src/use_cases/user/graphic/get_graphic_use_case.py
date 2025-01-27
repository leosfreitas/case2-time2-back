from repositories.graphic_repository import GraphicRepository
from fastapi import Request, Response
from entities.graphic import Graphic
import os
import jwt

class GetGraphic1UseCase:
    def __init__(self, graphic_repository: GraphicRepository):
        self.graphic_repository = graphic_repository

    def execute(self, response: Response, request: Request):
        token = request.cookies.get("user_auth_token")
        
        payload = jwt.decode(token.split(" ")[1], os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])
        user_id = payload.get("id")

        graphic = self.graphic_repository.get_graphic_categorias_x_despesas(user_id)
        if graphic is None:
            response.status_code = 200
            return []  

        response.status_code = 200
        return graphic
    
class GetGraphic2UseCase:
    def __init__(self, graphic_repository: GraphicRepository):
        self.graphic_repository = graphic_repository

    def execute(self, response: Response, request: Request):
        token = request.cookies.get("user_auth_token")
        
        payload = jwt.decode(token.split(" ")[1], os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])
        user_id = payload.get("id")

        graphic = self.graphic_repository.get_graphic_receitas_vs_despesas(user_id)
        if graphic is None:
            response.status_code = 200
            return []  

        response.status_code = 200
        return graphic
    
class GetGraphic3UseCase:
    def __init__(self, graphic_repository: GraphicRepository):
        self.graphic_repository = graphic_repository

    def execute(self, response: Response, request: Request):
        token = request.cookies.get("user_auth_token")
        
        payload = jwt.decode(token.split(" ")[1], os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])
        user_id = payload.get("id")

        graphic = self.graphic_repository.get_graphic_saldo_mensal(user_id)
        if graphic is None:
            response.status_code = 200
            return []  

        response.status_code = 200
        return graphic
    
class GetGraphic4UseCase:
    def __init__(self, graphic_repository: GraphicRepository):
        self.graphic_repository = graphic_repository

    def execute(self, response: Response, request: Request):
        token = request.cookies.get("user_auth_token")
        
        payload = jwt.decode(token.split(" ")[1], os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])
        user_id = payload.get("id")

        graphic = self.graphic_repository.get_graphic_orcamento_vs_gastos(user_id)
        if graphic is None:
            response.status_code = 200
            return []  

        response.status_code = 200
        return graphic