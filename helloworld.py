salutee = 'World'
saluter = 'Mina'

print('Hello {0}! I am {1}'.format(salutee, saluter))

# f"Hello {salutee}! I am {saluter}"
student_names = ["Mina", "Kaity", "Manal", "Za3bola"]
student_names.append("Magdi")

lyrics=["ard","tefa7ar","sa2f", "tema7ar", "jerken", "terken"]

print(len(student_names))
print(student_names)

student_names.append("Mirna")

print(len(student_names))
print(student_names)

del student_names[-1]
print(len(student_names))
print(student_names)

for name in student_names:
    print("Hello {0}! I am {1}".format(salutee,name))

for index in range(0,len(lyrics),2):
    print("Adik fel {0} {1}".format(lyrics[index], lyrics[index+1]))

for name in student_names:
    if name =="Za3bola":
        continue
    if name=="Manal":
        print("Found her!")
        break
    print(name + " . . .nope!")