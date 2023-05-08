from app.schema.schema_interface import SchemaInterface
from app.common.utils import is_substring_in_list


class CourseSchema(SchemaInterface):
    @staticmethod
    def to_dict(course, additional_columns, user):
        from app.common.model_schema_container.model_schema_container import ModelSchemaContainer
        course_dict = {
            'id': course.id,
            'title': course.title,
            'description': course.description,
        }

        if is_substring_in_list('lections', additional_columns):
            course_dict['lections'] = [
                ModelSchemaContainer.get_model_schema('lection').to_dict(lection, user=user)
                for lection in course.lections
            ]

        if is_substring_in_list('tests', additional_columns):
            test_additional_columns = []
            if is_substring_in_list('tests', additional_columns):
                additional_column = None
                for column in additional_columns:
                    if 'tests' in column:
                        additional_column = column
                        break

                if additional_column:
                    additional_column = additional_column[additional_column.find('.') + 1:]
                    test_additional_columns.append(additional_column)

            course_dict['tests'] = [
                ModelSchemaContainer.get_model_schema('test').to_dict(test, additional_columns=test_additional_columns)
                for test in course.tests
            ]

        if user:
            status = None
            for course_user in course.course_users:
                if course_user.user == user:
                    status = course_user.status.value
                    break
            course_dict['status'] = status

        return course_dict
