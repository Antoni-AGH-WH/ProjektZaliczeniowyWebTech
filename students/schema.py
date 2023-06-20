from enum import Enum

from pydantic import BaseModel
import random

possible_grades = [5.0,4.5,4.0,3.5,3.0,2.0]
def ID_maker(a):
    ID = ""
    for i in range(a):
        ID = ID + str(random.randint(0,9))
    ID = int(ID)
    return ID

class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str

    class Config:
        schema_extra = {"example": {"first_name": "Jerzetta","last_name": "Kłosińska",}}

class Student(BaseModel):
    id: int
    real_id: int
    first_name: str
    last_name: str

class StudentUpdateSchema(BaseModel):
    id: int
    real_id: int
    first_name: str
    last_name: str


class Mark(float, Enum):
    BARDZO_DOBRY = 5.0
    DOBRY_PLUS = 4.5
    DOBRY = 4.0
    DOSTATECZNY_PLUS = 3.5
    DOSTATECZNY = 3.0
    NIEDOSTATECZNY = 2.0

