import inspect

def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno


student = {"name":"Mark", "student_id":"15163", "feedback":None}

student["last_name"] = "Kowalski"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Key Not Found!")
except TypeError as error:
    print("You can't do that. . .moron!")
    print(error)
    print(lineno())
except Exception:
    print("Something wrong happened!")

print("This code executes")