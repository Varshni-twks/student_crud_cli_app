from dataclasses import dataclass, asdict
import json
import os

DATA_FILE = "students.json"
@dataclass
class Student:
    roll_no: str
    name: str
    standard: str

class Students:
    def __init__(self) -> None:
        self.students: list[Student] = []
        self.load_data()

    def show(self) -> list[Student]:
        print(len(self.students))
        return self.students
    
    def get(self, roll_no:str) -> Student | None:
        for student in self.students:
            if student.roll_no == roll_no:
                return student
        return None
    
    def add(self, student: Student) -> None:
        self.students.append(student)
        print(self.students)
        self.save_data()

    def delete(self, roll_no:str) -> None:
        student = self.get(roll_no)
        if student:
            self.students.remove(student)
            self.save_data()

    def update(self, new_student : Student) -> None:
        for i,student in enumerate(self.students):
            if student.roll_no == new_student.roll_no:
                self.students[i] = new_student
                self.save_data()
                break

    def load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE,'r') as f:
                    students_dict = json.load(f)
                self.students = [Student(**student) for student in students_dict]
            except json.JSONDecodeError:
                self.students = []
    
    def save_data(self):
        students_dict = [asdict(student) for student in self.students]
        with open(DATA_FILE, 'w') as f:
            json.dump(students_dict,f)
    
    

    