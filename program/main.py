# import os
# import sys

# # Add the path to the 'package' directory
# sys.path.append(os.path.join(os.path.dirname(__file__), '..\\package'))

# # Now you can import the module
# import module

# module.Hello('Jack')

# result = module.add_numbers(3, 5)
# print(result)  # This will print 8

# Result = module.multiplication(3, 3)
# print(Result)

#-----------------------
class Stack:
    def _init_(self):
        self.__stack_list = []

    def push(self,var):
        self.stack_list.append(var)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    
class Addingstack(Stack):
    def _init_(self):
        Stack._init_(self)
        self.__sum = 0
