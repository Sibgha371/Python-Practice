
# #Displaying a matrix
# def Display_matrix(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             print(matrix[i][j], end=" ")
#         print()

# #Multiplication of array with 2
# def miltiScalar(matrix):
#    for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             multiarray[i][j] = 2 * matrix[i][j]
#             # print(multiarray, end=" ")
#         print() 


# def Addition_array(matrix,array_1):
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             Add_array = matrix[i][j] + array_1[i][j]
#             print(Add_array, end=" ")
#         print()

# # Declaration of array A
# array_A = [
#     [1, 2],
#     [3, 4]
# ]

# # Declaration of array B
# array_B = [
#     [1, 0],
#     [0, 1]
# ]

# multiarray = [
#     [],
#     []
# ]

# Add_array = [
#     [],
#     []
# ]

# print("Matrix A")
# Display_matrix(array_A)
# print("Matrix B:")
# Display_matrix(array_B)
# print("Multiplication of 2 * B")
# miltiScalar(array_B)
# print(multiarray)
# # print("Adding [A + (2*B)]")
# # Addition_array(array_A,multiarray)



#Displaying a matrix
def Display_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=" ")
        print()

#Multiplication of array with 2
def miltiScalar(matrix):
   for i in range(len(matrix)):
        for j in range(len(matrix)):
            mulArray[i][j] = 2 * matrix[i][j]

def Addition_array(matrix,array_1):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            addArray[i][j] = matrix[i][j] + array_1[i][j]

# Declaration of array A
array_A = [
    [1, 2],
    [3, 4]
]

# Declaration of array B
array_B = [
    [1, 0],
    [0, 1]
]

# Declaration empty arrays for addition and multiplication
mulArray = [[0 for i in range(2)] for j in range(2)]
addArray = [[0 for i in range(2)] for j in range(2)]

print("Matrix A")
Display_matrix(array_A)

print("Matrix B")
Display_matrix(array_B)

print("Multiplication of 2 * B")
miltiScalar(array_B)
Display_matrix(mulArray)

print("Adding [A + (2*B)]")
Addition_array(array_A,mulArray)
Display_matrix(addArray)



