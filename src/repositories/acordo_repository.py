import os
import dotenv
from typing import List, Optional
from bson import ObjectId
from cryptography.fernet import Fernet

from models.acordo_model import AcordoModel
from models.fields.sensivity_field import SensivityField
from entities.acordo import Acordo

dotenv.load_dotenv()

class AcordoRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, acordo: Acordo) -> None:
        """
        Cria (ou atualiza) um registro de Acordo no MongoDB.
        """
        acordo_model = AcordoModel()
        acordo_dict = acordo.model_dump()

        # Preenche campos 'normais'
        for field in AcordoModel.get_normal_fields():
            if field in acordo_dict:
                acordo_model[field] = acordo_dict[field]

        # Preenche campos sensíveis (se houver)
        for field in AcordoModel.sensivity_fields:
            acordo_model[field] = SensivityField(
                fernet=self.fernet,
                data=acordo_dict[field]
            )

        acordo_model.save()

    def get_acordo_by_id(self, acordo_id: str) -> Optional[dict]:
        """
        Retorna o acordo em formato dict, ou None se não encontrado.
        """
        acordo_model = AcordoModel.objects.with_id(acordo_id)
        if not acordo_model:
            return None

        a_dict = acordo_model.to_mongo().to_dict()
        a_dict['_id'] = str(a_dict['_id'])
        return a_dict

    def get_all_acordos(self) -> List[dict]:
        """
        Retorna todos os acordos em formato de lista de dicionários.
        """
        acordos = AcordoModel.objects
        acordos_list = []
        for a in acordos:
            a_dict = a.to_mongo().to_dict()
            a_dict['_id'] = str(a_dict['_id'])
            acordos_list.append(a_dict)
        return acordos_list

    def delete_acordo_by_id(self, acordo_id: str) -> bool:
        """
        Deleta um acordo pelo ID.
        Retorna True se encontrou e deletou, False caso contrário.
        """
        acordo_model = AcordoModel.objects.with_id(acordo_id)
        if not acordo_model:
            return False
        acordo_model.delete()
        return True

    def get_acordos_by_user_id(self, user_id: str) -> List[dict]:
        """
        Retorna todos os acordos de um usuário específico.
        """
        acordos = AcordoModel.objects(user_id=user_id)
        result = []
        for a in acordos:
            a_dict = a.to_mongo().to_dict()
            a_dict["_id"] = str(a_dict["_id"])
            result.append(a_dict)
        return result
    
    def get_acordos_by_users(self, user_ids: List[str]) -> List[dict]:
        """
        Retorna todos os acordos cujos user_id estejam na lista user_ids.
        """
        acordos = AcordoModel.objects(user_id__in=user_ids)
        result = []
        for a in acordos:
            a_dict = a.to_mongo().to_dict()
            a_dict["_id"] = str(a_dict["_id"])
            result.append(a_dict)
        return result