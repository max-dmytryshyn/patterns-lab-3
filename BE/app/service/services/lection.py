from app.common.model_schema_container.model_schema_container import ModelSchemaContainer


class LectionService:
    model_manager = ModelSchemaContainer.get_model_manager('lection')
    schema = ModelSchemaContainer.get_model_schema('lection')

    @classmethod
    def get_all_lections(cls):
        lections = []
        for lection in cls.model_manager.get_all_with_filter():
            lections.append(cls.schema.to_dict(lection))
        return lections

    @classmethod
    def create_lection(cls, data):
        lection = cls.model_manager.create(data)
        return cls.schema.to_dict(lection)

    @classmethod
    def get_lection_by_id(cls, id):
        lection = cls.model_manager.get_by_id(id=id)
        return cls.schema.to_dict(lection)

    @classmethod
    def update_lection(cls, id, data):
        lection = cls.model_manager.update_by_id(id=id, data=data)
        return cls.schema.to_dict(lection)

    @classmethod
    def delete_lection_by_id(cls, id):
        lection = cls.model_manager.delete_by_id(id=id)
        return cls.schema.to_dict(lection, additional_columns=['course'])
