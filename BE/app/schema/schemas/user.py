from app.schema.schema_interface import SchemaInterface
from app.common.utils import is_substring_in_list


class UserSchema(SchemaInterface):
    @staticmethod
    def to_dict(user, additional_columns, _):
        from app.common.model_schema_container.model_schema_container import ModelSchemaContainer
        user_dict = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
        }

        if is_substring_in_list('courses', additional_columns):
            course_additional_columns = []
            if is_substring_in_list('courses.lections', additional_columns):
                additional_column = None
                for column in additional_columns:
                    if 'courses.lections' in column:
                        additional_column = column
                        break

                if additional_column:
                    additional_column = additional_column[additional_column.find('.') + 1:]
                    course_additional_columns.append(additional_column)

            if is_substring_in_list('courses.tests', additional_columns):
                additional_column = None
                for column in additional_columns:
                    if 'courses.tests' in column:
                        additional_column = column
                        break

                if additional_column:
                    additional_column = additional_column[additional_column.find('.') + 1:]
                    course_additional_columns.append(additional_column)

            courses_dict = []
            courses = [uc.course for uc in user.user_courses]
            for course in courses:
                course_dict = ModelSchemaContainer.get_model_schema('course').to_dict(course, additional_columns=course_additional_columns, user=user)
                courses_dict.append(course_dict)
            user_dict['courses'] = courses_dict

        return user_dict
