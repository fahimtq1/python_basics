# Functions

# Basic function
def greet_user():
    first_name, last_name = input("Please enter your full name: ").split()
    full_name = ("%s %s" % (first_name.capitalize(), last_name.capitalize()))
    return print(f"Welcome {full_name}!")

# Create a basic calculator

class calc:
    def add(a, b):
        '''Function that adds the inputs'''
        return a + b

    def subtract(a, b):
        '''Function that divides the inputs'''
        return a - b

    def multiply(a, b):
        '''Function that multiplies the inputs'''
        return a * b

    def divide(a, b):
        '''Function that divides the inputs'''
        return a / b




