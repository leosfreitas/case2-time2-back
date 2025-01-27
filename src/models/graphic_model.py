from mongoengine import *
import datetime
from models.fields.sensivity_field import SensivityField
import os
import dotenv
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class GraphicModel(Document):
    sensivity_fields = [
    ]

    dados = DictField(required=True)

    def get_normal_fields():
        return [
            i
            for i in GraphicModel.__dict__.keys()
            if i[:1] != "_" and i != "sensivity_fields" and i not in GraphicModel.sensivity_fields
        ]
