from mongoengine import *
import datetime
from models.fields.sensivity_field import SensivityField
import os
import dotenv
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class FinanceModel(Document):
    sensivity_fields = [
    ]

    categoria = StringField(
        required=True,
        choices=[
            "Receita",
            "Despesa"
        ]
    )
    user = StringField(required=False)
    tipo = StringField(required=True)
    valor = StringField(required=True)
    data = StringField(required=True)
    descricao = StringField(required=False)

    def get_normal_fields():
        return [
            i
            for i in FinanceModel.__dict__.keys()
            if i[:1] != "_" and i != "sensivity_fields" and i not in FinanceModel.sensivity_fields
        ]
