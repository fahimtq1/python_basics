# Functions

# Basic function
def greet_user():
    first_name, last_name = input("Please enter your full name: ").split()
    full_name = ("%s %s" % (first_name.capitalize(), last_name.capitalize()))
    return print(f"Welcome {full_name}!")

# Create a function that takes two arguments and adds them
def add(a,b):
    return print(a + b)

