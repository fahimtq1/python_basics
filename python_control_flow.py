# Control flow

## if, elif, else
weather = "sunny"
if weather == "sunny":   # True or False will determine the command that is run
    print("Let's do a BBQ")
elif weather == "dry":
    print("Getting there")
else:
    print("Hope for the best")

## loops
shopping_list = {"item 1":"fruits","item 2":"milks","item 3":"cream","item 4":"bread","item 5":"cereal","item 6":"toothbrush"}
print("Number of items in shopping list:", len(shopping_list))
print()
print("Shopping list:")
for item in shopping_list:
    print(shopping_list[item].capitalize())
print()
print(shopping_list.keys())
print(shopping_list.values())
print()
print("Shopping list items:")
for item in shopping_list:
    print(item.capitalize(),"-",shopping_list[item].capitalize())



