from typer import Typer
from student import Students, Student

app = Typer()

students_object = Students()



@app.command()
def show():
    students = students_object.show()
    print("ROLL NO \t | NAME \t | STANDARD \t |")
    for student in students:
        print(f"{student.roll_no} \t | {student.name} \t | {student.standard} \t |")


@app.command()
def get(roll_no: str):
    student = students_object.get(roll_no)
    if student:
        print(f"{student.roll_no} \t | {student.name} \t | {student.standard} \t |")
    else:
        print("No student found with given roll Number")


@app.command()
def add():
    name = input("Enter student Name:")
    roll_no = input("Enter student roll number:")
    standard = input("Enter standard(I to XII):")

    students_object.add(Student(roll_no=roll_no, name=name, standard=standard))


if __name__ == "__main__":
    app()
