import os
import dotenv
from typing import List, Optional
from mongoengine import DoesNotExist
from cryptography.fernet import Fernet
from bson import ObjectId

from models.contato_model import ContatoModel
from models.fields.sensivity_field import SensivityField
from entities.contato import Contato

dotenv.load_dotenv()

class ContatoRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, contato: Contato) -> None:
        contato_model = ContatoModel()
        contato_dict = contato.model_dump()

        for k in ContatoModel.get_normal_fields():
            if k not in contato_dict:
                continue

            contato_model[k] = contato_dict[k]

        for k in ContatoModel.sensivity_fields:
            contato_model[k] = SensivityField(fernet=self.fernet, data=contato_dict[k])

        contato_model.save()

        return None

    def get_contato_by_id(self, contato_id: str) -> Optional[dict]:
        """
        Retorna o contato em formato dict, ou None se não encontrado.
        """
        try:
            contato = ContatoModel.objects.with_id(contato_id)
        except (DoesNotExist, ValueError):
            return None
        
        if not contato:
            return None

        contato_dict = contato.to_mongo().to_dict()
        contato_dict['_id'] = str(contato_dict['_id'])
        return contato_dict

    def get_all_contatos(self) -> List[dict]:
        """
        Retorna uma lista de dicionários com todos os contatos.
        """
        contatos = ContatoModel.objects
        contatos_dict = []
        for c in contatos:
            c_dict = c.to_mongo().to_dict()
            c_dict['_id'] = str(c_dict['_id'])
            contatos_dict.append(c_dict)
        return contatos_dict

    def delete_contato_by_id(self, contato_id: str) -> bool:
        """
        Deleta o contato pelo ID. 
        Retorna True se deletou, False se não encontrou.
        """
        contato = ContatoModel.objects.with_id(contato_id)
        if not contato:
            return False
        contato.delete()
        return True

    def update_contato_resposta(self, contato_id: str, resposta: str) -> bool:
        """
        Atualiza apenas o campo 'resposta' do contato.
        Retorna True se o contato foi encontrado e atualizado.
        """
        # Verifica se contato_id é um ObjectId válido
        try:
            object_id = ObjectId(contato_id)
        except:
            return False

        contato_model = ContatoModel.objects.with_id(object_id)
        if not contato_model:
            return False

        contato_model.resposta = resposta
        contato_model.save()
        return True

    def get_contato_by_user_id(self, user_id: str) -> Optional[dict]:
        """
        Retorna o contato em formato dict, ou None se não encontrado.
        """
        try:
            contato = ContatoModel.objects.get(user_id=user_id)
        except DoesNotExist:
            return None
        
        if not contato:
            return None

        contato_dict = contato.to_mongo().to_dict()
        contato_dict['_id'] = str(contato_dict['_id'])
        return contato_dict