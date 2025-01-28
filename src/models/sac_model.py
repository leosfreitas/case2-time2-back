from mongoengine import *
import datetime
from models.fields.sensivity_field import SensivityField
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class SacModel(Document):
    sensivity_fields = [
        
    ]

    nome = StringField(required=True)
    email = StringField(required=True)
    motivo = StringField(required=True)
    mensagem = StringField(required=True)

    def get_normal_fields():
        return [i for i in SacModel.__dict__.keys() if i[:1] != '_' and i != "sensivity_fields" and i not in SacModel.sensivity_fields]
    
    def get_decrypted_field(self, field: str):
        if field not in self.sensivity_fields:
            raise Exception("Field not mapped")

        return fernet.decrypt(getattr(self, field, None).token).decode()