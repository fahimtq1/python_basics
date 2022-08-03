# Python collections tutorial

# Lists
shopping_list = ["bat","milk","bread","controller","juice","tooth brush"]   # build a shopping list

for item in shopping_list:   # for loop iterating through the shopping list to print each item separately
    print(item.capitalize())

print(shopping_list)
print(len(shopping_list))   # length of shopping_list
print(type(shopping_list))   # type of variable that shopping_list is

shopping_list.append("toys")   # appending an item to the end of a list
shopping_list.remove("milk")   # removing an item from a list
print(shopping_list)

# Tuples
coordinates = (1,2,3)   # coordinates in a tuple

for position in coordinates:
    print(position)

print(coordinates)
print(len(coordinates))
print(type(coordinates))

# Dictionaries
devops_student_1 = {
    "key" : "value",
    "name" : "James",
    "stream" : "tech",
    "completed_lessons" : 3,   # dictionary storing different data types
    "completed_lessons_names" : ["lists", "operations", "builtin methods"]   # dictionary storing different collection types
}

print(devops_student_1)
print(len(devops_student_1))   # returns the number of key:value pairs
print(type(devops_student_1))
print(devops_student_1["completed_lessons_names"])   # calling the name key to show to corresponding value
print(devops_student_1.keys())   # return the dictionary keys
print(devops_student_1.values())   # return the dictionary values

## How to change completed_lessons from 3 to 2
devops_student_1["completed_lessons"] = 2

## Dictionary delete items
del devops_student_1["stream"]   # deletes an item from the dictionary using the key "stream"
devops_student_1.clear()   # clears all the items in a dictionary
devops_student_1.pop("stream")   # method that deletes an item from the dictionary using the key "stream"
devops_student_1.popitem()   # method that removes the last item in a dictionary

# Control flow
weather = "sunny"
if weather == "sunny":   # True or False will determine the command that is run
    print("Let's do a BBQ")
elif weather == "dry":
    print("Getting there")
else:
    print("Hope for the best")



