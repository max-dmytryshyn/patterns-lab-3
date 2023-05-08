from abc import abstractmethod


class SchemaInterface:
    @staticmethod
    @abstractmethod
    def to_dict(data, additional_columns, user):
        pass


class SchemaManager:
    def __init__(self, schema_class: SchemaInterface):
        self.schema_class = schema_class

    def to_dict(self, data, additional_columns=None, user=None):
        if data is None:
            return None
        if additional_columns is None:
            additional_columns = []
        dict = self.schema_class.to_dict(data, additional_columns, user)
        return dict
