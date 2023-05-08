from app.common.model_schema_container.config import MODELS_MAP
from app.data_layer.model_interface import ModelManager
from app.schema.schema_interface import SchemaManager


class ModelSchemaContainer:
    @staticmethod
    def get_model_manager(model_key):
        model_dict = MODELS_MAP.get(model_key)
        if model_dict is None:
            raise RuntimeError(f"No model info found for {model_key}")
        return ModelManager(model_dict['model_class'])

    @staticmethod
    def get_model_schema(model_key):
        model_dict = MODELS_MAP.get(model_key)
        if model_dict is None:
            raise RuntimeError(f"No model info found for {model_key}")
        return SchemaManager(model_dict['schema_class'])
