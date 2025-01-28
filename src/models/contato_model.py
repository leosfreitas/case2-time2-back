import os
import dotenv
from mongoengine import Document, StringField
from cryptography.fernet import Fernet
from models.fields.sensivity_field import SensivityField

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class ContatoModel(Document):
    sensivity_fields = [
    ]

    user_id = StringField(required=True)
    email = StringField(required=True)
    mensagem = StringField(required=True)
    resposta = StringField(required=False)

    @staticmethod
    def get_normal_fields():
        """
        Retorna todos os campos 'comuns' 
        (ou seja, que não são sensíveis e nem atributos internos).
        """
        return [
            i
            for i in ContatoModel.__dict__.keys()
            if i[:1] != '_' 
            and i != "sensivity_fields" 
            and i not in ContatoModel.sensivity_fields
        ]

    def get_decrypted_field(self, field: str):
        """
        Descriptografa um campo declarado em 'sensivity_fields'.
        Se o campo não estiver mapeado, dispara um Exception.
        """
        if field not in self.sensivity_fields:
            raise Exception("Field not mapped")

        # Obtém o conteúdo encriptado e descriptografa
        encrypted_value = getattr(self, field, None)
        if not encrypted_value:
            return None

        return fernet.decrypt(encrypted_value.token).decode()
