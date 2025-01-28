from repositories.contato_repository import ContatoRepository
from fastapi import Request, Response
import os

class GetAllContatosUseCase:
    def __init__(self, contatos_repository: ContatoRepository):
        self.contatos_repository = contatos_repository

    def execute(self, response: Response, request: Request):
      
        todos_contatos = self.contatos_repository.get_all_contatos()

        contatos_por_usuario = {}
        for contato in todos_contatos:
            user_id = contato["user_id"]
            if user_id not in contatos_por_usuario:
                contatos_por_usuario[user_id] = []
            contatos_por_usuario[user_id].append(contato)

        response.status_code = 200
        return contatos_por_usuario
