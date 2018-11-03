students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    for student_title in students_titlecase:
        print(student_title)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)

def save_file(student_name):
    try:
        f = open("students.txt","a")
        f.write(student_name + "\n")
        f.close()
    except Exception as error:
        print("Could not save to file")
        print(error)

def read_file():
    try:
        f = open("students.txt","r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception as error:
        print("Could not read from file")
        print(error)

read_file()
print_students_titlecase()

student_name = input("Please enter the student name: ")
student_ID = input("Please enter the student ID: ")

add_student(student_name, student_ID)
save_file(student_name)



#def var_args(name, *args):
#    print(name)
#    print(args)


#def var_args2(name, **kwargs):
#    print (name)
#    print(kwargs["description"], kwargs["feedback"])

# add_student(name="Mark", student_id=15)
#
# var_args("Mark", "Loves Python", None, "Hello", True)
# var_args2("Mark", description = "Loves Python", feedback = None, pluralsight_subscrber=True)