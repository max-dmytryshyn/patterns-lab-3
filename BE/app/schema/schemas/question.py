from app.schema.schema_interface import SchemaInterface
from app.common.utils import is_substring_in_list


class QuestionSchema(SchemaInterface):
    @staticmethod
    def to_dict(question, additional_columns, user):
        from app.common.model_schema_container.model_schema_container import ModelSchemaContainer
        question_dict = {
            'id': question.id,
            'text': question.text,
        }

        if is_substring_in_list('answers', additional_columns):
            question_dict['answers'] = [ModelSchemaContainer.get_model_schema('answer').to_dict(answer) for answer in question.answers]

        return question_dict
