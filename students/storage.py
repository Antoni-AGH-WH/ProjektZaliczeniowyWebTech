from functools import lru_cache

STUDENTS = {}
GRADES = {}

@lru_cache()
def get_students():
    return STUDENTS

@lru_cache()
def get_grades():
    return GRADES