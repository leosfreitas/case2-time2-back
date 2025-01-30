import os
import bcrypt
import dotenv
from typing import List, Optional
from mongoengine import *
from cryptography.fernet import Fernet
from entities.user import User
from models.user_model import UserModel
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash

class UsersRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, user: User) -> None:
        user_model = UserModel()
        user_dict = user.model_dump()

        for k in UserModel.get_normal_fields():
            if k not in user_dict:
                continue
            user_model[k] = user_dict[k]

        for k in UserModel.sensivity_fields:
            user_model[k] = SensivityField(fernet=self.fernet, data=user_dict[k])

        user_model.password = bcrypt.hashpw(f'{user.password}'.encode(), bcrypt.gensalt()).decode()

        if user.tipo == "Pessoa":
            user_model.cpf = user_dict["cpf"]
            user_model.cnpj = None
        elif user.tipo == "Empresa":
            user_model.cnpj = user_dict["cnpj"]
            user_model.cpf = None

        user_model.save()

        return None
    
    def find_by_email(self, email: str) -> list[UserModel]:
        result = UserModel.objects(email=email)
        return result
    
    def find_by_id(self, id: str) -> list[UserModel]:
        result = UserModel.objects(id=id)
        return result
    
    def update_reset_pwd_token(self, email: str, sent_at: int, token: str) -> None:
        UserModel.objects(email=email).update(set__reset_pwd_token_sent_at=sent_at, set__reset_pwd_token=token)

        return None
    
    def find_by_reset_pwd_token(self, token) -> list[UserModel]:
        result: list[UserModel] = UserModel.objects(reset_pwd_token=token)

        return result
    
    def update_pwd(self, id: str, pwd: str) -> None:
        UserModel.objects(id=id).update(set__password = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode())

        return None
    
    def get_name(self, id: str) -> str:
        user = UserModel.objects(id=id).first()
        if user:
            return user.name

    def get_email(self, id: str) -> str:
        user = UserModel.objects(id=id).first()
        if user:
            return user.email
        
    def get_cpf(self, id: str) -> str:
        user = UserModel.objects(id=id).first()
        if user:
            return user.cpf
        
    def get_cnpj(self, id: str) -> str:
        user = UserModel.objects(id=id).first()
        if user:
            return user.cnpj
        
    def find_by_cpf(self, cpf: str) -> Optional[UserModel]:
        return UserModel.objects(cpf=cpf).first()

    def find_by_cnpj(self, cnpj: str) -> Optional[UserModel]:
        return UserModel.objects(cnpj=cnpj).first()
        
    def get_phone(self, id: str) -> str:
        user = UserModel.objects(id=id).first()
        if user:
            return user.phone
        
    def get_password(self, id: str) -> str:
        user = UserModel.objects(id=id).first()
        if user:

            return self.fernet.decrypt(user.password).decode()
        
    def get_tipo(self, id: str) -> str:
        user = UserModel.objects(id=id).first()
        if user:
            return user.tipo
    
    def update_name(self, id: str, name: str) -> None:
        UserModel.objects(id=id).update(set__name = name)
        return None

    def update_email(self, id: str, email: str) -> None:
        UserModel.objects(id=id).update(set__email = email)
        return None
    
    def update_cpf(self, id: str, cpf: str) -> None:
        UserModel.objects(id=id).update(set__cpf = cpf)
        return None
    
    def update_phone(self, id: str, phone: str) -> None:
        UserModel.objects(id=id).update(set__phone = phone)
        return None

    
    def get_all_users(self) -> List[dict]:
        users = UserModel.objects
        users_dict = [user.to_mongo().to_dict() for user in users]
        for user in users_dict:
            user['_id'] = str(user['_id'])
        return users_dict

    def delete_user_by_id(self, user_id: str) -> bool:
        user = UserModel.objects.with_id(user_id)
        if not user:
            return False
        user.delete()
        return True