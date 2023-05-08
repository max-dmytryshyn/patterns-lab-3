from enum import Enum


class ActivityStatus(Enum):
    NOT_ACTIVE = 'NOT_ACTIVE'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'


class TestType(Enum):
    PRACTISE = 'PRACTISE'
    EXAM = 'EXAM'
