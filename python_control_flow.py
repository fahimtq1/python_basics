# Control flow

## if, elif, else
weather = "sunny"
if weather == "sunny":   # True or False will determine the command that is run
    print("Let's do a BBQ")
elif weather == "dry":
    print("Getting there")
else:
    print("Hope for the best")

print()

## loops
### for loops
shopping_list = {"item 1":"fruits",
                 "item 2":"milks",
                 "item 3":"cream",
                 "item 4":"bread",
                 "item 5":"cereal",
                 "item 6":"toothbrush"
                 }   # creating a shopping list in dictionary format
print("Number of items in shopping list:", len(shopping_list))   # printing the number of key:value pairs
print()
print("Shopping list:")
for item in shopping_list:   # iterating through shopping_list and prints each value
    print(shopping_list[item].capitalize())
print()
for item in shopping_list:   # iterating through shopping_list and prints each key
    print(item.capitalize())
print()
print("Shopping list items:")
for item in shopping_list:   # iterates through shopping_list to print each key with its corresponding value
    print(item.capitalize(),"-",shopping_list[item].capitalize())

print()

# Use case of multiple conditions
# Create a list with integer values 1-4
data_list = [1,2,3,4]
# Iterate through the list using for loop
for i in data_list:
# Find 3 and print if found
    if i == 3:
        print("Found 3")
# Or else list number greater than 3 print gone too far
    elif i > 3:
        print("Gone too far")
# Otherwise print too soon
    else:
        print("Gone too soon")

print()

### while loops
number = 0
# iterate while number is less than 10
while number < 10:
# print the number with message stating "it's working"
    print(f"{number}- it's working")
# +1 in each iteration
    number += 1

# while user enters anything but integers, continue to prompt with message requesting correct input
user_prompt = True
while user_prompt:
    age = input("Please enter your age: ")
    if age.isdigit():
        if 0 < int(age) < 117:
            user_prompt = False   # stop prompting the user
            print(f"Your age is {age}")
        else:
            print("Please enter a valid age")
    else:
        print("Please enter an integer number")


'''
Explaining the while loop:
- You begin with a condition (in this case the condition is stored in the variable user_prompt
- Whilst the condition is met it will run the code
- If statement to check 
'''



