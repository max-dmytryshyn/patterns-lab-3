from abc import abstractmethod


class ModelInterface:
    @staticmethod
    @abstractmethod
    def get_all_with_filter(filter):
        pass

    @staticmethod
    @abstractmethod
    def get_by_id(id):
        pass

    @staticmethod
    @abstractmethod
    def create(data):
        pass

    @staticmethod
    @abstractmethod
    def create_many(data):
        pass

    @staticmethod
    @abstractmethod
    def update_by_id(id, data):
        pass

    @staticmethod
    @abstractmethod
    def delete_by_id(id):
        pass


class ModelManager:
    def __init__(self, model_class: ModelInterface):
        self.model_class = model_class

    def get_all_with_filter(self, filter=None):
        if filter is None:
            filter = {}
        return self.model_class.get_all_with_filter(filter)

    def get_by_id(self, id):
        return self.model_class.get_by_id(id)

    def create(self, data):
        return self.model_class.create(data)

    def create_many(self, data):
        return self.model_class.create_many(data)

    def update_by_id(self, id, **data):
        return self.model_class.update_by_id(id, **data)

    def delete_by_id(self, id):
        return self.model_class.delete_by_id(id)
