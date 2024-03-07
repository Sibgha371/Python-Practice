# lst = [1, 2, 3, 4, 5]
# lst_2 = []
# add = 0

# for number in lst:
#     add += number
#     print(number)
#     lst_2.append(add)


# print(lst_2)
#------------------------------------------------
# vehicles_one = ['car', 'bicycle', 'motor']
# print(vehicles_one) # outputs: ['car', 'bicycle', 'motor']

# vehicles_two = vehicles_one
# del vehicles_one[0] # deletes 'car'
# print(vehicles_two) # outputs: ['bicycle', 'motor']
#-------------------------------------------------

# vals = [0, 1, 2]
# vals[0], vals[2] = vals[2], vals[0]
# print(vals)
# -------------------------------------------------------------------

# myList = [0, 1, 2, 3]
# x = 1
# for elem in myList:
#     x *=elem
# print(x)
#---------------------------------------------------------

# i = 2
# while i>=0:
#     print("*")
#     i-= 2
#----------------------------------------------------------

# myList = [1, 2, 3, 4]
# print(myList[-3:-2])
#-----------------------------------------------------------

# a = 1
# b = 0
# c = a & b 
# d = a | b
# e = a ^ b

# print(c + d + e)
#------------------------------------------------------------

# myList = [[0,1,2,3] for i in range(2)]
# print(myList[2][0])
#-----------------------------------------------

# var = 1
# while var < 10:
#     print("#")
#     var = var << 1
#--------------------------------------------------------

# myList = [1,2,3]
# for v in range(len(myList)):
#     myList.insert(1,myList[v])
# print(myList)
#----------------------------------------------------------

# t = [[3-i for i in range(3)] for j in range(3)]
# s= 0
# for i in range(3):
#     s += t[i][i]
# print(s)
#  ----------------------------------------------------

# var = 0
# while var < 6:
#     var +=1
#     if var % 2 == 0:
#         continue
#     print("#")
#-------------------------------------------------------

# for i in range(1):
#     print("#")
# else:
#     print("#")
#--------------------------------------------------------

# i = 0
# while i <= 5:
#     i += 1
#     if i % 2 == 0:
#         break 
#     print("*")
#----------------------------------------------------------

# def wishes():
#     return "Happy Birthday!"

# print(wishes())

#     # outputs: Happy Birthday!
#----------------------------------------------------------
# def create_list(n):
#     my_list = []
#     for i in range(n):
#         my_list.append(i)
#     return my_list

# print(create_list(5))
#----------------------------------\

# foo = (1,2,3)
# foo.index(0)
#-----------------------------------------------

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2

# print(fun(fun(2)))
#------------------------------------------------------------

# def fun(inp=2, out=3):
#     return inp * out

# print(fun(out=2))
#-----------------------------------------------------------------

# def fun1(a):
#     return None
# def fun2(a):
#     return fun1(a) * fun1(a)

# print(fun2(2))
#------------------------------------------------------------
# list = [0,0,0,0,0]
# list = [i for i in range(-1, -2)]
# print(list)
#-----------------------------------------------

# nums = [1,2,3]
# vals = nums[-1:-2]
# print(vals)
# print(nums)
#----------------------------------------------

# def fun(x):
#     global y
#     y = x * x
#     return y

# fun(2)
# print(y)
#--------------------------------------------------

# def fun(a, b):
#     return a ** a

# print(fun(2))
#----------------------------------------------------

myList = ['mary', 'had', 'a', 'little', 'lamb']

def myList(myList):
    del myList[3]
    myList[3] = 'ram'

print(myList(myList))


