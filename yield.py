students = []

def read_file():
    try:
        f = open("students.txt","r")
        for student in f.readlines():
            students.append(student)
        f.close()
    except FileNotFoundError as error:
        print(error)

read_file()
print(students)
