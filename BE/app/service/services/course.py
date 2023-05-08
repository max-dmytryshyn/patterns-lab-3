from app.common.model_schema_container.model_schema_container import ModelSchemaContainer


class CourseService:
    model_manager = ModelSchemaContainer.get_model_manager('course')
    schema = ModelSchemaContainer.get_model_schema('course')

    @classmethod
    def get_all_courses(cls):
        courses = []
        for course in cls.model_manager.get_all_with_filter():
            courses.append(cls.schema.to_dict(course))
        return courses

    @classmethod
    def create_course(cls, data):
        course = cls.model_manager.create(data)
        return cls.schema.to_dict(course)

    @classmethod
    def get_course_by_id(cls, id):
        course = cls.model_manager.get_by_id(id=id)
        return cls.schema.to_dict(course)

    @classmethod
    def update_course(cls, id, data):
        course = cls.model_manager.update_by_id(id=id, data=data)
        return cls.schema.to_dict(course)

    @classmethod
    def delete_course_by_id(cls, id):
        course = cls.model_manager.delete_by_id(id=id)
        return cls.schema.to_dict(course)
