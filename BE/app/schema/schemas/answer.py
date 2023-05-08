from app.schema.schema_interface import SchemaInterface


class AnswerSchema(SchemaInterface):
    @staticmethod
    def to_dict(answer, additional_columns, user):
        answer_dict = {
            'id': answer.id,
            'text': answer.text,
            'is_right': answer.is_right
        }

        return answer_dict
