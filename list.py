student_name = []
num = int(input("Enter the number of students: "))
for i in range(num):
    msg = "Enter the name of" + str(i+1) + "Student: "
    x = input(msg)
    student_name.append(x)
print(student_name)
print(len(student_name))


