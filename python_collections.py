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
