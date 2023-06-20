from fastapi import APIRouter, HTTPException

from students.schema import StudentUpdateSchema, Student, StudentCreateSchema, ID_maker, possible_grades, Mark
from students.storage import get_students, get_grades

router = APIRouter()

@router.get("/")
async def fetch_student():
    return get_students()

@router.post("/")
async def create_student(student: StudentCreateSchema):
    id = len(get_students()) + 1
    real_id = ID_maker(2)
    new_student = Student(**student.dict(), id=id, real_id = real_id)
    get_students()[id] = new_student
    get_grades()[id] = []
    return new_student

@router.get("/<id>") #szukanie studenta po ID
async def find_student_by_id(item_id: int):
    if item_id not in get_students():
        raise HTTPException(status_code=404, detail="Student not found")
    return {"Student ID": get_students()[item_id]}

@router.post("/<id>")
#Program pobiera 3 informacje: ID którego studenta ma zmodyfikować, oraz nowe imie i nazwisko
async def modify_student(item_id: int, first_name:str, last_name: str):
    #jeżeli nie ma ID - wywala error
    if item_id not in get_students():
        raise HTTPException(status_code=404, detail="Student not found")
    #tworzymy nowego studenta, który zastąpi starego
    new_student = StudentUpdateSchema(first_name = first_name, last_name = last_name, id=item_id, real_id = ID_maker(2))
    #nowe dane studenta zastępują dane stare
    get_students()[item_id] = new_student
    #w przypadku sukcesu - wyświetlają się nowe dane
    return {"Student ID:": get_students()[item_id]}


@router.post("/<id>/grade")
async def assign_grade(student_id: int, grade: float):
    if student_id not in get_grades():
        raise HTTPException(status_code=404, detail="Student not found")
    if grade in possible_grades:
        nowe_oceny = Mark(grade)
        get_grades()[student_id] += [nowe_oceny]
    else:
        raise HTTPException(status_code=505, detail="Wrong grade! You can't do that")
    return {"Student ID:": get_grades()[student_id]}


@router.get("/<id>/grade")
async def show_grades(student_id: int):
    if student_id not in get_grades():
        raise HTTPException(status_code=404, detail="Student not found")
    if len(get_grades()[student_id]) == 0:
        return {"Student ID": "Student doesn't have any grades yet"}
    else:
        return {"Student ID": get_grades()[student_id]}

#/students/{student_id}/marks/{ocena}