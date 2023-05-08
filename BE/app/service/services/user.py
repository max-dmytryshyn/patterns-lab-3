from app.common.model_schema_container.model_schema_container import ModelSchemaContainer


class UserService:
    model_manager = ModelSchemaContainer.get_model_manager('user')
    schema = ModelSchemaContainer.get_model_schema('user')

    @classmethod
    def get_all_users(cls):
        users = []
        for user in cls.model_manager.get_all_with_filter():
            users.append(cls.schema.to_dict(user, additional_columns=['courses.lections', 'courses.tests.questions.answers']))
        return users

    @classmethod
    def create_user(cls, data):
        user = cls.model_manager.create(data)
        return cls.schema.to_dict(user)

    @classmethod
    def get_user_by_id(cls, id):
        user = cls.model_manager.get_by_id(id=id)
        return cls.schema.to_dict(user)

    @classmethod
    def update_user(cls, id, data):
        user = cls.model_manager.update_by_id(id=id, data=data)
        return cls.schema.to_dict(user)

    @classmethod
    def delete_user_by_id(cls, id):
        user = cls.model_manager.delete_by_id(id=id)
        return cls.schema.to_dict(user)

    @classmethod
    def add_user_to_course(cls, data):
        ModelSchemaContainer.get_model_manager('user_course').create(data)
        user = cls.model_manager.get_by_id(data['user_id'])
        return cls.schema.to_dict(user, additional_columns=['courses.lections', 'courses.tests.questions.answers'])
