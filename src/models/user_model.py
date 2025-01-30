from mongoengine import *
import datetime
from models.fields.sensivity_field import SensivityField
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class UserModel(Document):
    sensivity_fields = [
        # Adicione aqui os campos sensíveis que precisam de criptografia, como 'cpf' ou 'cnpj'
    ]

    tipo = StringField(required=True, choices=["Pessoa", "Empresa"])
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True, unique=True)
    cpf = StringField()  # CPF só será preenchido se tipo == Pessoa
    cnpj = StringField()  # CNPJ só será preenchido se tipo == Empresa
    phone = StringField(required=True)

    reset_pwd_token = StringField(default="")
    reset_pwd_token_sent_at = IntField(default=0)

    @classmethod
    def get_normal_fields(cls):
        return [
            field for field in cls._fields.keys()
            if field not in cls.sensivity_fields and field != "_id"
        ]

    def clean(self):
        """
        Validação customizada para garantir que apenas CPF ou CNPJ sejam definidos.
        """
        if self.tipo == "Pessoa" and not self.cpf:
            raise ValidationError("O campo 'cpf' é obrigatório para usuários do tipo 'Pessoa'.")
        if self.tipo == "Empresa" and not self.cnpj:
            raise ValidationError("O campo 'cnpj' é obrigatório para usuários do tipo 'Empresa'.")
        if self.tipo == "Pessoa" and self.cnpj:
            raise ValidationError("Usuários do tipo 'Pessoa' não devem ter o campo 'cnpj'.")
        if self.tipo == "Empresa" and self.cpf:
            raise ValidationError("Usuários do tipo 'Empresa' não devem ter o campo 'cpf'.")
        
    def get_decrypted_field(self, field: str):
        if field not in self.sensivity_fields:
            raise Exception("Field not mapped")

        return fernet.decrypt(getattr(self, field, None).token).decode()

    def check_password_matches(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))