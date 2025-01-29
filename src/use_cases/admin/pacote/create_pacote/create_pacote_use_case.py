from fastapi import Request, Response
from repositories.pacote_repository import PacoteRepository
from entities.pacote import Pacote
from .create_pacote_dto import CreatePacoteDTO

class CreatePacoteUseCase:
    def __init__(self, pacote_repository: PacoteRepository):
        self.pacote_repository = pacote_repository

    def execute(self, create_pacote_dto: CreatePacoteDTO, response: Response, request: Request):
        # Cria o Pydantic Pacote (que roda a validação do .model_validator)
        pacote = Pacote(
            tipo=create_pacote_dto.tipo,
            cliente=create_pacote_dto.cliente,
            preco=create_pacote_dto.preco,
            cortesia=create_pacote_dto.cortesia,
            nome=create_pacote_dto.nome,
            detalhes=create_pacote_dto.detalhes
        )
        # Salva no repositório (que agora armazena tudo como dict)
        self.pacote_repository.save(pacote)
        response.status_code = 200
        return {"status": "success", "message": "Pacote criado com sucesso"}
