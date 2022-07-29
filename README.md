# Python and Pycharm installation

## Installing Python

- Follow the following URL to [download Python](https://www.python.org/downloads/), and it will take you to a webpage below: 
![image](https://user-images.githubusercontent.com/99980305/181736492-45e69d04-f699-4b69-8d4c-165cd9533f71.png)
- The website should automatically recognise your OS, but if doesn't ensure you download using the correct link for your respective operatin system
- The installer for Python should pop up:
![image](https://user-images.githubusercontent.com/99980305/181737570-ba6209a1-fe3e-4397-a3cd-ef73fd0c999c.png)
- Select "Customize installation" and then "Add to PATH" to make sure you can access Python directly from the default directory without having to navigate to the one its saved in
- Complete the steps and now you have Python installed!

## Installing Pycharm

- Follow the following URL to [download Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows):
![image](https://user-images.githubusercontent.com/99980305/181738298-ea83cd6f-a91d-4f27-9fd3-ea64e5378279.png)
- Select the "Community Edition" and your download will begin
- To set up Pycharm ensure that the interpreter is using the latest version of Python installed on your local host
- You can now use Pycharm as a Python interpreter!

## Example Python code

# Learning about Python variables

```{python}
print("Hello World")   # testing PyCharm

'''
What are variables?
- The shorthand for variables is var
- They store data of different types

Types of variables:
- int
- float
- boolean
- string
'''

# Example variables with input()
print("Welcome!")

print("Please enter your first name")
first_name = input()
print(first_name)
print(type(first_name))

print("Please enter your last name")
last_name = input()
print(last_name)
print(type(last_name))

print("Please enter your age")
age = int(input())
print(age)
print(type(age))

print("Please enter your post code")
post_code = input()
print(post_code)
print(type(post_code))

print("Please enter your course")
course = input()
print(course)
print(type(course))

print("Please enter your salary")
salary = float(input())
print(salary)
print(type(salary))
```
