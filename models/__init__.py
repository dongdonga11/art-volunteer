from datetime import datetime
from bson import ObjectId

class School:
    def __init__(self, name, location, type):
        self.name = name
        self.location = location
        self.type = type

    @staticmethod
    def from_db_object(db_object):
        if db_object:
            db_object['id'] = str(db_object.pop('_id'))
        return db_object

class Volunteer:
    def __init__(self, school_id, user_id, priority=False):
        self.school_id = school_id
        self.user_id = user_id
        self.priority = priority
        self.created_at = datetime.utcnow()

    def to_dict(self):
        return {
            'school_id': self.school_id,
            'user_id': self.user_id,
            'priority': self.priority,
            'created_at': self.created_at
        }

    @staticmethod
    def from_db_object(db_object):
        if db_object:
            db_object['id'] = str(db_object.pop('_id'))
        return db_object 