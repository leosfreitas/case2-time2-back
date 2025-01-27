import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.finance import Finance
from models.finance_model import FinanceModel
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash
from bson import ObjectId

class FinanceRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, finance: Finance) -> None:
        finance_model = FinanceModel()
        finance_dict = finance.model_dump()

        for k in FinanceModel.get_normal_fields():
            if k not in finance_dict:
                continue

            finance_model[k] = finance_dict[k]

        for k in FinanceModel.sensivity_fields:
            finance_model[k] = SensivityField(fernet=self.fernet, data=finance_dict[k])

        finance_model.save()

        return None

    def get_finance_by_id(self, finance_id: str) -> dict:
        finance = FinanceModel.objects.with_id(finance_id)
        if not finance:
            return None
        finance_dict = finance.to_mongo().to_dict()
        finance_dict['_id'] = str(finance_dict['_id'])
        return finance_dict
    
    def get_finance_by_user_id(self, user: str) -> List[dict]:
        finances = FinanceModel.objects(user=user)
        if not finances:
            return None

        finances_list = []
        for finance in finances:
            finance_dict = finance.to_mongo().to_dict()
            finance_dict['_id'] = str(finance_dict['_id'])  
            finances_list.append(finance_dict)
        
        return finances_list
    
    def get_despesas_by_user_id(self, user: str) -> List[dict]:
        finances = FinanceModel.objects(user=user, categoria='Despesa')
        if not finances:
            return None

        finances_list = []
        for finance in finances:
            finance_dict = finance.to_mongo().to_dict()
            finance_dict['_id'] = str(finance_dict['_id'])  
            finances_list.append(finance_dict)
        
        return finances_list
        
    def get_receitas_by_user_id(self, user: str) -> List[dict]:
        finances = FinanceModel.objects(user=user, categoria='Receita')
        if not finances:
            return None

        finances_list = []
        for finance in finances:
            finance_dict = finance.to_mongo().to_dict()
            finance_dict['_id'] = str(finance_dict['_id'])  
            finances_list.append(finance_dict)
        
        return finances_list

    
    def delete_finance_by_id(self, finance_id: str, user: str) -> bool:
        finance = FinanceModel.objects.with_id(finance_id)
        if not finance:
            return False
        if finance.user != user:
            return False
        finance.delete()
        return True
    
    def update_finance(self, finance_id: str, tipo: str, valor: float, data: str, descricao: str) -> bool:
        if not ObjectId.is_valid(finance_id):
            return False

        finance_model = FinanceModel.objects.with_id(ObjectId(finance_id))
        if not finance_model:
            return False

        if tipo:
            finance_model.tipo = tipo
        if valor:
            finance_model.valor = valor
        if data:
            finance_model.data = data
        if descricao:
            finance_model.descricao = descricao

        finance_model.save()
        return True