from fastapi import Response
from repositories.user_repository import UsersRepository

class GetUsersUseCase:
    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    def execute(self, response: Response):
        """
        Executa a lógica para buscar todos os usuários.
        """
        users = self.user_repository.get_all_users()
        response.status_code = 200  # Define explicitamente o status de sucesso
        return users
