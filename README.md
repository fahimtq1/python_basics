# Python introduction

## Python variables

What are variables?
- The shorthand for variables is var
- They store data of different types

Types of variables:
- int
- float
- boolean
- string

## Operators

There are two types of operators. 

### Arithmetic operators:
- ```+``` 
- ```-```
- ```*```
- ```/```

### Comparison operators:
- `<`
- `>`
- `==`
- `!=`
- `<=`
- `>=`

## Collections:

There are three types of data collections in Python:
- Lists
- Tuples
- Dictionaries

### Lists

What are lists?
- Lists are a type of collection denoted by ```[]```
- Lists are mutable (they can be changed)
- Lists are flexible as they can take different data types
- Indexing lists follows the typical Python indexing convention (see my slicing tutorial [here](https://github.com/fahimtq1/user_details/blob/main/README.md))

List examples:

The following example demonstrates a list being stored as a variable called ```shopping_list```

```python
shopping_list = ["bat","milk","bread","controller","juice","tooth brush"]
```

You append an item to the end of a list with the ```.append()``` method

```python
shopping_list.append("toys")
```

You can remove an item from a list with the ```.remove()``` method:

```python
shopping_list.remove("milk")   
```

### Tuples 

What are tuples?
- Tuples are a type of collection denoted by ```()```
- Tuples are immutable (they can't be changed)
- Indexing tuples follows the typical Python indexing convention

Tuple examples:

The following example demonstrates a coordinate stored as tuple in Python:

```python
coordinates = (1,2,3) 
```

### Dictionaries

What are dictionaries?
- Dictionaries are a type of collection denoted by ```{}```
- They are key:value pairs: you call a key from the dictionary to return the corresponding value
- 






