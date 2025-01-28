from mongoengine import *
import datetime
from models.fields.sensivity_field import SensivityField
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class AcordoModel(Document):
    sensivity_fields = [
        
    ]

    user_id = StringField(required=True)
    pacote_id = StringField(required=True)

    def get_normal_fields():
        return [i for i in AcordoModel.__dict__.keys() if i[:1] != '_' and i != "sensivity_fields" and i not in AcordoModel.sensivity_fields]
    
    def get_decrypted_field(self, field: str):
        if field not in self.sensivity_fields:
            raise Exception("Field not mapped")

        return fernet.decrypt(getattr(self, field, None).token).decode()