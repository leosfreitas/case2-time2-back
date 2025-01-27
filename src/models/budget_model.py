from mongoengine import *
import os, dotenv
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class BudgetModel(Document):
    sensivity_fields = []

    user = StringField(required=True)
    tipo = StringField(
        required=True,
        choices=[
            "Habitação",
            "Transporte",
            "Alimentação",
            "Saúde",
            "Educação",
            "Lazer",
            "Roupas",
            "Tecnologia",
            "Assinaturas e Serviços",
            "Investimentos",
            "Doações",
            "Impostos",
            "Dívidas",
            "Outros"
        ]
    )
    valor = StringField(required=True)

    meta = {'collection': 'budgets'}

    def get_normal_fields():
        return [
            i for i in BudgetModel.__dict__.keys()
            if i[:1] != "_" and i != "sensivity_fields" and i not in BudgetModel.sensivity_fields
        ]
