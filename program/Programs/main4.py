# original_list = ['omega', 'beta', 'gamma', 'alpha']
# new_list = sorted(original_list)

# print(original_list)
# print(new_list)
# print()
# originalList = ['omega', 'beta', 'gamma', 'alpha']
# print (originalList)
# originalList.sort()
# print (originalList)


# s1 = 'Where are the snows of yesteryear?'
# s2 = s1.split()
# s3 = sorted(s2)
# print(s3)
# print(s3[1])      


# Define LED patterns for each digit (0-9)
# digits = [
#     ["###", "# #", "# #", "# #", "###"],
#     ["  #", "  #", " # ", "  #", "###"],
#     ["###", "  #", "###", "#  ", "###"],
#     ["###", "  #", "###", "  #", "###"],
#     ["# #", "# #", "###", "  #", "  #"],
#     ["###", "#  ", "###", "  #", "###"],
#     ["###", "#  ", "###", "# #", "###"],
#     ["###", "  #", "  #", "  #", "  #"],
#     ["###", "# #", "###", "# #", "###"],
#     ["###", "# #", "###", "  #", "###"]
# ]

# # Get user input as a string
# user_input = input("Enter a non-negative integer: ")

# Display the LED pattern for each digit in the input
# for digit in user_input:
#     if digit.isdigit():
#         pattern = digits[int(digit)]
#         for row in pattern:
#             print(row)

# Caeser cipher encripting messages-------------
# text = input("Enter your masseage: ")
# cispher = ''
# for char in text:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char)+1
#     if code > ord('Z'):
#         code = ord('A')
#     cispher += chr(code)
# print(cispher)

# Caeser cipher dencripting messages-------------
# cispher = input("Enter your cryptogram: ")
# text = ''
# for char in cispher:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char)-1
#     if code < ord('Z'):
#         code = ord('A')
#     text += chr(code)

# print(text)


#Numbers processor.
# line = input("Enter the line of numbers -- seperating them with spaces: ")
# string = line.split()
# total = 0
# try:
#     for substr in string:
#         total += float(substr)
#         print("The total is :",total)
# except:
#     print(substr, "is not a number")

#The IBAN Validator
# IBAN Validator.

# iban = input("Enter IBAN, please: ")
# iban = iban.replace(' ','')

# if not iban.isalnum():
#     print("You have entered invalid characters.")
# elif len(iban) < 15:
#     print("IBAN entered is too short.")
# elif len(iban) > 31:
#     print("IBAN entered is too long.")
# else:
#     iban = (iban[4:] + iban[0:4]).upper()
#     iban2 = ''
#     for ch in iban:
#         if ch.isdigit():
#             iban2 += ch
#         else:
#             iban2 += str(10 + ord(ch) - ord('A'))
#     iban = int(iban2)
#     if iban % 97 == 1:
#         print("IBAN entered is valid.")
#     else:
#         print("IBAN entered is invalid.")

#Incript message by shifting
# def caesar_cipher(text, shift):
#     result = ""
#     for char in text:
#         if char.isalpha():
#             is_upper = char.isupper()
#             shifted = ord(char) + shift
#             if is_upper:
#                 if shifted > ord('Z'):
#                     shifted -= 26
#             else:
#                 if shifted > ord('z'):
#                     shifted -= 26
#             result += chr(shifted)
#         else:
#             result += char
#     return result

# def get_valid_shift():
#     while True:
#         try:
#             shift = int(input("Enter a shift value (1-25): "))
#             if 1 <= shift <= 25:
#                 return shift
#             else:
#                 print("Shift value must be between 1 and 25.")
#         except ValueError:
#             print("Invalid input. Please enter an integer.")

# text = input("Enter a line of text to encrypt: ")
# shift = get_valid_shift()
# encrypted_text = caesar_cipher(text, shift)
# print("Encrypted text:", encrypted_text)

#--------------if the texts srer anagrams-------------------

# 
#---------------Digit of life----------------
# def digit_of_life(date):
#     while len(date) > 1:
#         total = 0
#         for digit in date:
#             total += int(digit)
#         date = str(total)
#     return date

# # Input from the user
# date = input("Enter your birthday (YYYYMMDD, YYYYDDMM, or MMDDYYYY): ")

# # Remove any non-digit characters from the input
# date = ''.join(filter(str.isdigit, date))

# # Calculate the Digit of Life
# result = digit_of_life(date)

# print("Digit of Life:", result)

'''--------- 
a game are the characters comprising the 
 string hidden inside the second string?
first--------------'''
# def are_characters_hidden(word, text):
#     word = word.lower()
#     text = text.lower()
    
#     word_index = 0
#     for char in text:
#         if char == word[word_index]:
#             word_index += 1
#             if word_index == len(word):
#                 return "Yes"
    
#     return "No"

# # Input from the user
# word = input("Enter a word: ")
# text = input("Enter a text: ")

# result = are_characters_hidden(word, text)
# print(result)

#---------Sudoku is a number-placing puzzle played on a 9x9 board.------------
def is_valid_sudoku(board):
    # Check rows and columns
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            if board[i][j] in row or board[j][i] in col:
                return "No"
            row.add(board[i][j])
            col.add(board[j][i])

    # Check sub-squares
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_square = set()
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    if board[x][y] in sub_square:
                        return "No"
                    sub_square.add(board[x][y])

    return "Yes"

# Input Sudoku as a list of lists
sudoku = []
for _ in range(9):
    row = input()
    sudoku.append([int(digit) for digit in row])

result = is_valid_sudoku(sudoku)
print(result)

