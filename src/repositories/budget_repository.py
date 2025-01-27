import os, dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.budget import Budget
from models.budget_model import BudgetModel
from models.fields.sensivity_field import SensivityField
from bson import ObjectId

dotenv.load_dotenv()

class BudgetRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, budget: Budget) -> None:
        budget_model = BudgetModel()
        budget_dict = budget.model_dump()

        for k in BudgetModel.get_normal_fields():
            if k not in budget_dict:
                continue
            budget_model[k] = budget_dict[k]

        for k in BudgetModel.sensivity_fields:
            budget_model[k] = SensivityField(fernet=self.fernet, data=budget_dict[k])

        budget_model.save()

    def get_budget_by_id(self, budget_id: str) -> dict:
        budget = BudgetModel.objects.with_id(budget_id)
        if not budget:
            return None
        budget_dict = budget.to_mongo().to_dict()
        budget_dict['_id'] = str(budget_dict['_id'])
        return budget_dict

    def get_budgets_by_user_id(self, user: str) -> List[dict]:
        budgets = BudgetModel.objects(user=user)
        if not budgets:
            return []
        
        budgets_list = []
        for budget in budgets:
            budget_dict = budget.to_mongo().to_dict()
            budget_dict['_id'] = str(budget_dict['_id'])
            budgets_list.append(budget_dict)
        return budgets_list

    def delete_budget_by_id(self, budget_id: str, user: str) -> bool:
        budget = BudgetModel.objects.with_id(budget_id)
        if not budget:
            return False
        if budget.user != user:
            return False
        budget.delete()
        return True
