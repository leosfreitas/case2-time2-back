from mongoengine import (
    Document,
    StringField,
    ListField,
    DictField,
    ValidationError,
)
import os
import dotenv

dotenv.load_dotenv()


class PacoteModel(Document):
    # Se você não vai usar _id manual, pode deixar o ObjectId padrão
    # _id = ObjectIdField(primary_key=True)  # se quiser explicitamente

    tipo = ListField(
        StringField(choices=["Residencial", "Movel", "Fixa"]),
        required=True
    )
    preco = StringField(required=True)
    cortesia = StringField(required=False)
    nome = StringField(required=True)

    # Agora como DictField
    detalhes = DictField(required=False)

    def clean(self):
        """
        Validação customizada antes de salvar o documento no MongoDB.
        Verificamos se 'detalhes' contém as chaves mínimas, etc.
        """
        # Para cada tipo na lista 'tipo':
        for t in self.tipo:
            # Se for Fixa, não exige detalhes
            if t == "Fixa":
                continue

            # Se for Residencial ou Movel, detalhes são obrigatórios
            if t not in self.detalhes or not self.detalhes[t]:
                raise ValidationError(f"Detalhes para o tipo '{t}' são obrigatórios.")

            # Verificamos se 'detalhes[t]' é realmente um dict (pode ter vindo algo malformado)
            if not isinstance(self.detalhes[t], dict):
                raise ValidationError(
                    f"Detalhes para o tipo '{t}' devem ser um dicionário com campos específicos."
                )

            # Checa campos essenciais para Residencial
            if t == "Residencial":
                subdoc = self.detalhes[t]
                if "velocidade" not in subdoc or "tipo" not in subdoc:
                    raise ValidationError(
                        "Detalhes do tipo 'Residencial' devem conter os campos 'velocidade' e 'tipo'."
                    )

            # Checa campos essenciais para Movel
            elif t == "Movel":
                subdoc = self.detalhes[t]
                if "tamanho_do_plano" not in subdoc or "tipo" not in subdoc:
                    raise ValidationError(
                        "Detalhes do tipo 'Movel' devem conter os campos 'tamanho_do_plano' e 'tipo'."
                    )

        # Verifica se há tipos em 'detalhes' que não estão na lista 'tipo'
        for key in self.detalhes.keys():
            if key not in self.tipo:
                raise ValidationError(f"Tipo '{key}' em 'detalhes' não está em 'tipo'.")

    @staticmethod
    def get_normal_fields():
        """
        Exemplo de função que retorna campos não sensíveis do modelo.
        """
        return [
            field
            for field in PacoteModel._fields.keys()
            if field not in ["sensivity_fields"]  # ou alguma lógica
        ]
