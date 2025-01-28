from typing import List, Optional, Union, Dict
from bson import ObjectId
from mongoengine import ValidationError
from models.pacote_model import PacoteModel
from entities.pacote import Pacote, Residencial, Movel, Fixa


class PacoteRepository:
    def save(self, pacote: Pacote) -> None:
        pacote_model = PacoteModel()
        pacote_dict = pacote.model_dump()

        # Preenche os campos do PacoteModel
        for field in PacoteModel._fields.keys():
            if field in pacote_dict:
                # Quando for 'detalhes', agora é só um dict
                if field == "detalhes":
                    pacote_model.detalhes = pacote_dict["detalhes"]
                else:
                    pacote_model[field] = pacote_dict[field]

        pacote_model.save()  # dispara o .clean() também
        return None
    


    def get_pacote_by_id(self, pacote_id: str) -> Optional[dict]:
        if not ObjectId.is_valid(pacote_id):
            return None

        pacote = PacoteModel.objects.with_id(pacote_id)
        if not pacote:
            return None

        pacote_dict = pacote.to_mongo().to_dict()
        pacote_dict["_id"] = str(pacote_dict["_id"])
        return pacote_dict

    def get_all_pacotes(self) -> List[dict]:
        pacotes = PacoteModel.objects()
        pacotes_list = [
            {**pacote.to_mongo().to_dict(), "_id": str(pacote.id)} for pacote in pacotes
        ]
        return pacotes_list

    def get_pacotes_by_tipo(self, tipo: str) -> List[dict]:
        pacotes = PacoteModel.objects(tipo=tipo)
        pacotes_list = [
            {**pacote.to_mongo().to_dict(), "_id": str(pacote.id)} for pacote in pacotes
        ]
        return pacotes_list

    def delete_pacote_by_id(self, pacote_id: str) -> bool:
        pacote = PacoteModel.objects.with_id(pacote_id)
        if not pacote:
            return False
        pacote.delete()
        return True

    def update_pacote(
        self,
        pacote_id: str,
        tipo: Optional[List[str]] = None,
        preco: Optional[str] = None,
        cortesia: Optional[str] = None,
        nome: Optional[str] = None,
        detalhes: Optional[Dict[str, dict]] = None,
    ) -> bool:
        # Converte pacote_id para ObjectId
        try:
            object_id = ObjectId(pacote_id)
        except Exception:
            return False

        # Busca o pacote pelo ID
        pacote_model = PacoteModel.objects.with_id(object_id)
        if not pacote_model:
            return False

        # Atualiza os campos enviados
        if tipo:
            pacote_model.tipo = tipo
        if preco:
            pacote_model.preco = preco
        if cortesia:
            pacote_model.cortesia = cortesia
        if nome:
            pacote_model.nome = nome
        if detalhes:
            pacote_model.detalhes = detalhes

        pacote_model.save()  # Salva no banco
        return True

