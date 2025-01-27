from fastapi import FastAPI
from mongoengine import connect
from fastapi.middleware.cors import CORSMiddleware
import os
import glob
import dotenv
from importlib import import_module

dotenv.load_dotenv()

connect(host=f"mongodb+srv://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PWD')}@insperjr.irxsm.mongodb.net/")

app = FastAPI()

@app.get("/")
def test():
    return {"status": "OK v2 (3)"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],          # URL do front-end permitido
    allow_credentials=True,                  # Permitir envio de cookies ou headers de autenticação
    allow_methods=["*"],                     # Permitir todos os métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],                     # Permitir todos os headers
)

# Obtém o diretório atual onde o arquivo app.py está localizado
working_directory = os.path.dirname(os.path.abspath(__file__))

# Define o caminho para o diretório onde os "use_cases" (casos de uso) estão localizados
use_cases_directory = os.path.join(working_directory, "use_cases")

# Procura recursivamente por arquivos index.py dentro dos diretórios de casos de uso
routes = glob.glob(os.path.join(use_cases_directory, "**/index.py"), recursive=True)

# Importa e registra automaticamente as rotas definidas em cada arquivo index.py
for route in routes:
    # Converte o caminho do arquivo em um nome de módulo relativo
    relative_path = os.path.relpath(route, working_directory)
    module_name = os.path.splitext(relative_path)[0].replace(os.path.sep, '.')
    try:
        # Importa dinamicamente o módulo
        module = import_module(module_name)
        # Se o módulo possui um objeto 'router', inclui as rotas no aplicativo FastAPI
        if hasattr(module, 'router'):
            app.include_router(module.router)
    except ModuleNotFoundError as e:
        # Exibe uma mensagem de erro caso o módulo não seja encontrado
        print(f"Erro ao importar módulo {module_name}: {e}")