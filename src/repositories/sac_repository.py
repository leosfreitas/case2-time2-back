import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.sac import Sac

from models.sac_model import SacModel

from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash
from bson import ObjectId

class SacRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, sac: Sac) -> None:
        sac_model = SacModel()
        sac_dict = sac.model_dump()

        for k in SacModel.get_normal_fields():
            if k not in sac_dict:
                continue

            sac_model[k] = sac_dict[k]

        for k in SacModel.sensivity_fields:
            sac_model[k] = SensivityField(fernet=self.fernet, data=sac_dict[k])

        sac_model.save()

        return None

    def get_sac_by_id(self, sac_id: str) -> dict:
        sac = SacModel.objects.with_id(sac_id)
        if not sac:
            return None
        sac_dict = sac.to_mongo().to_dict()
        sac_dict['_id'] = str(sac_dict['_id'])
        return sac_dict