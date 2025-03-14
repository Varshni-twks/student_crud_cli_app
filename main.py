from typer import Typer
from student import Students, Student

app = Typer()

students_object = Students()



@app.command()
def show():
    students = students_object.show()
    print(f"{"ROLL NO":<15} | {"NAME":<15} | {"STANDARD":<15} |")
    print("-"*53)
    for student in students:
        print(f"{student.roll_no:<15} | {student.name:<15} | {student.standard:<15} |")


@app.command()
def get(roll_no: str):
    student = students_object.get(roll_no)
    if student:
        print(f"{student.roll_no:<15} | {student.name:<15} | {student.standard:<15} |")
    else:
        print("No student found with given roll Number")


@app.command()
def add():
    name = input("Enter student Name:")
    roll_no = input("Enter student roll number:")
    standard = input("Enter standard(I to XII):")

    students_object.add(Student(roll_no=roll_no, name=name, standard=standard))

@app.command()
def update():
    name = input("Enter student Name:")
    roll_no = input("Enter student roll number:")
    standard = input("Enter standard(I to XII):")

    students_object.update(Student(roll_no=roll_no, name=name, standard=standard))

@app.command()
def delete(roll_no: str):
    students_object.delete(roll_no)

if __name__ == "__main__":
    app()
