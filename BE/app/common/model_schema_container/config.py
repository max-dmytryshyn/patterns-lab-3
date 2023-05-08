from app.data_layer import User, Course, Lection, Test, Question, Answer, UserCourse
from app.schema import UserSchema, CourseSchema, LectionSchema, TestSchema, QuestionSchema, AnswerSchema

MODELS_MAP = {
    'user': {
        'model_class': User,
        'schema_class': UserSchema,
    },
    'course': {
        'model_class': Course,
        'schema_class': CourseSchema,
    },
    'lection': {
        'model_class': Lection,
        'schema_class': LectionSchema,
    },
    'test': {
        'model_class': Test,
        'schema_class': TestSchema,
    },
    'question': {
        'model_class': Question,
        'schema_class': QuestionSchema,
    },
    'answer': {
        'model_class': Answer,
        'schema_class': AnswerSchema,
    },
    'user_course': {
        'model_class': UserCourse,
        'schema_class': None,
    },
}
