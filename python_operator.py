# Python operators tutorial

# Functions method builtin python

print(greeting.isalpha())
print(greeting.islower())
print(greeting.isupper())
print(greeting.isdigit())
print(greeting.startswith("H"))
print(greeting.endswith("d"))

# Indexing
greeting = "Hello World"
print(len(greeting))
print(greeting[-5])   # W
print(greeting[5])   #
print(greeting[:5])   # Hello
print(greeting[5:])

# Indexing and slicing exercise
print(greeting[6:])
print(greeting[3])
print(greeting[:7])
print(greeting[:6])

# String methods
random_text = "Lot's of text but why do I text so much"
print(random_text)
print(random_text.upper())
print(random_text.capitalize())   # this makes the first letter of the string a capital letter
print(random_text.lower())
print(random_text.count("text"))
print((random_text.replace("Lot's","Lots")))

# Concatenation and casting
first_name = 'James'
middle_name = 'Bond'
last_name = '007'
age = 47
print(first_name + ' ' + middle_name + ' ' + last_name + ' ' + str(age))




