from app.schema.schema_interface import SchemaInterface
from app.common.utils import is_substring_in_list


class TestSchema(SchemaInterface):
    @staticmethod
    def to_dict(test, additional_columns, user):
        from app.common.model_schema_container.model_schema_container import ModelSchemaContainer
        test_dict = {
            'id': test.id,
            'title': test.title,
            'description': test.description,
        }

        if is_substring_in_list('course', additional_columns):
            test_dict['course'] = ModelSchemaContainer.get_model_schema('course').to_dict(test.course)

        if is_substring_in_list('questions', additional_columns):
            question_additional_columns = ['answers'] if is_substring_in_list('questions.answers', additional_columns) else []
            test_dict['questions'] = [
                ModelSchemaContainer.get_model_schema('question').to_dict(question, additional_columns=question_additional_columns)
                for question in test.questions
            ]

        if user:
            status = None
            for test_user in test.test_users:
                if test_user.user == user:
                    status = test_user.status.value
                    break
            test_dict['status'] = status

        return test_dict
