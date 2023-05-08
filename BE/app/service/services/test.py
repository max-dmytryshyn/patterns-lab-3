from app.common.model_schema_container.model_schema_container import ModelSchemaContainer


class TestService:
    model_manager = ModelSchemaContainer.get_model_manager('test')
    schema = ModelSchemaContainer.get_model_schema('test')

    @classmethod
    def get_all_tests(cls):
        tests = []
        for test in cls.model_manager.get_all_with_filter():
            tests.append(cls.schema.to_dict(test))
        return tests

    @classmethod
    def create_test(cls, data):
        test = cls.model_manager.create(data)
        return cls.schema.to_dict(test)

    @classmethod
    def get_test_by_id(cls, id):
        test = cls.model_manager.get_by_id(id=id)
        return cls.schema.to_dict(test)

    @classmethod
    def update_test(cls, id, data):
        test = cls.model_manager.update_by_id(id=id, data=data)
        return cls.schema.to_dict(test)

    @classmethod
    def delete_test_by_id(cls, id):
        test = cls.model_manager.delete_by_id(id=id)
        return cls.schema.to_dict(test)
