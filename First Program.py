student_name = ["Hamza" , "Atsha" , "Ali" , "Muniba" , 1]
student_name[4] = "Zunaira"
print(student_name[4])
for e in student_name:
    print(e , end = "     ")
#If we want to print the particular index then
print()
for e in student_name[4]:
    print(e , end = "     ")
print()

#Take input in the lis
num = int(input("Enter the number of students: "))
for i in range(num):
    msg = "Enter the name of" + str(i+1) + " Student: "
    x = input(msg)
    student_name.append(x)
print(student_name)

#total 
myList = [10, 3, 15, 6, 18]
total = 0

if i in myList:
    total += i
print(total)


