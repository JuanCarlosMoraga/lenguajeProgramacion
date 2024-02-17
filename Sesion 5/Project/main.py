from classes import student

student1 = student(1, "Jose", "ISI")
student2 = student(1, "Maria", "Derecho")
student3 = student(1, "Marco", "ISI")

students = []
students.append(student1)
students.append(student2)
students.append(student3)

#mostra lista
for stu in students:
    print(stu)