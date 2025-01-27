import os
import bcrypt
import dotenv
from typing import List, Optional
from mongoengine import *
from cryptography.fernet import Fernet
from entities.graphic import Graphic
from models.finance_model import FinanceModel
from models.budget_model import BudgetModel
from models.graphic_model import GraphicModel
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash
from bson import ObjectId
from collections import defaultdict
from datetime import datetime
from typing import Optional
import locale

class GraphicRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, graphic: Graphic) -> None:
        graphic_model = GraphicModel()
        graphic_dict = graphic.model_dump()

        for k in GraphicModel.get_normal_fields():
            if k not in graphic_dict:
                continue

            graphic_model[k] = graphic_dict[k]

        for k in GraphicModel.sensivity_fields:
            graphic_model[k] = SensivityField(fernet=self.fernet, data=graphic_dict[k])

        graphic_model.save()

        return None
    
    def get_graphic_categorias_x_despesas(self, user: str) -> Optional[Graphic]:
        finances = FinanceModel.objects(user=user, categoria='Despesa')
        if not finances:
            return None

        dados = {}
        for data in finances:
            graphic_dict = data.to_mongo().to_dict()
            
            tipo = graphic_dict.get('tipo')
            valor = graphic_dict.get('valor', 0)

            try:
                dados[tipo] = float(valor)
            except (ValueError, TypeError):
                dados[tipo] = 0.0 

        return Graphic(dados=dados)
    
    def get_graphic_receitas_vs_despesas(self, user: str) -> Optional[Graphic]:
        finances = FinanceModel.objects(user=user)
        if not finances:
            return None

        receitas_total = 0.0
        despesas_total = 0.0

        for data in finances:
            graphic_dict = data.to_mongo().to_dict()
            
            categoria = graphic_dict.get('categoria', '').lower()
            valor = graphic_dict.get('valor', 0)

            try:
                valor_float = float(valor)
            except (ValueError, TypeError):
                valor_float = 0.0

            if categoria == 'receita':
                receitas_total += valor_float
            elif categoria == 'despesa':
                despesas_total += valor_float

        dados = {
            'receitas': receitas_total,
            'despesas': despesas_total
        }

        return Graphic(dados=dados)

    locale.setlocale(locale.LC_TIME, "pt_BR.utf8")

    def get_graphic_saldo_mensal(self, user: str) -> Optional[Graphic]:
        finances = FinanceModel.objects(user=user)
        if not finances:
            return None

        saldo_mensal = defaultdict(float) 
        for data in finances:
            graphic_dict = data.to_mongo().to_dict()
            
            categoria = graphic_dict.get('categoria', '').lower()
            valor = graphic_dict.get('valor', 0)
            data_str = graphic_dict.get('data', '')

            try:
                valor_float = float(valor)
            except (ValueError, TypeError):
                valor_float = 0.0

            try:
                data_obj = datetime.strptime(data_str, "%Y-%m-%d")
                mes_nome = data_obj.strftime("%B").capitalize()  
            except (ValueError, TypeError):
                continue  

            if categoria == 'receita':
                saldo_mensal[mes_nome] += valor_float
            elif categoria == 'despesa':
                saldo_mensal[mes_nome] -= valor_float

        saldo_mensal_dict = dict(saldo_mensal)

        return Graphic(dados=saldo_mensal_dict)
    
    def get_graphic_orcamento_vs_gastos(self, user: str) -> Optional[Graphic]:
        finances = FinanceModel.objects(user=user, categoria='Despesa')
        budgets = BudgetModel.objects(user=user)
        if not finances or not budgets:
            return None

        orcamento_por_categoria = {
            budget.tipo.lower(): float(budget.valor)
            for budget in budgets
        }

        gastos_por_categoria = defaultdict(float)

        for data in finances:
            graphic_dict = data.to_mongo().to_dict()
            
            tipo = graphic_dict.get('tipo', '').lower()
            valor = graphic_dict.get('valor', 0)

            try:
                valor_float = float(valor)
            except (ValueError, TypeError):
                valor_float = 0.0

            if tipo in orcamento_por_categoria:
                gastos_por_categoria[tipo] += valor_float

        dados = {}
        for tipo in orcamento_por_categoria:
            dados[f"orcamento_{tipo}"] = orcamento_por_categoria.get(tipo, 0.0)
            dados[f"despesas_{tipo}"] = gastos_por_categoria.get(tipo, 0.0)

        return Graphic(dados=dados)