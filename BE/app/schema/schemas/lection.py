from app.schema.schema_interface import SchemaInterface
from app.common.utils import is_substring_in_list


class LectionSchema(SchemaInterface):
    @staticmethod
    def to_dict(lection, additional_columns, user):
        from app.common.model_schema_container.model_schema_container import ModelSchemaContainer
        lection_dict = {
            'id': lection.id,
            'title': lection.title,
            'description': lection.description,
            'text': lection.text,
            'video_url': lection.video_url
        }

        if is_substring_in_list('course', additional_columns):
            lection_dict['course'] = ModelSchemaContainer.get_model_schema('course').to_dict(lection.course)

        if user:
            status = None
            for lection_user in lection.lection_users:
                if lection_user.user == user:
                    status = lection_user.status.value
                    break
            lection_dict['status'] = status

        return lection_dict
