from dataclasses import dataclass


@dataclass
class Student:
    roll_no: str
    name: str
    standard: str

class Students:
    def __init__(self) -> None:
        self.students: list[Student] = []

    def show(self) -> list[Student]:
        return self.students
    
    def get(self, roll_no:int) -> Student | None:
        for student in self.students:
            if student.roll_no == roll_no:
                return student
        return None
    
    def add(self, student: Student) -> None:
        self.students.append(student)

    def delete(self, roll_no:int) -> None:
        student = self.get(roll_no)
        if student:
            self.students.remove(student)

    def update(self, new_student : Student) -> None:
        for student in self.students:
            if student.roll_no == new_student.roll_no:
                student = new_student
                break
    

    