# Introduction to Python

Let's go through some basic Python syntax, covering variables, data types, loops, and conditionals with examples and explanations.

### 1. Variables

Variables are used to store data that can be used and manipulated throughout your program. In Python, you don't need to declare the type of a variable explicitly; it is inferred from the value you assign to it.

```python
# Example of variables
x = 10          # Integer
y = 3.14        # Float
name = "Alice"  # String
is_student = True  # Boolean

print(x)        # Output: 10
print(y)        # Output: 3.14
print(name)     # Output: Alice
print(is_student)  # Output: True
```

### 2. Data Types

Python has several built-in data types, including integers, floats, strings, and booleans. Here are some examples:

```python
# Integer
a = 5
print(type(a))  # Output: <class 'int'>

# Float
b = 3.14
print(type(b))  # Output: <class 'float'>

# String
c = "Hello, World!"
print(type(c))  # Output: <class 'str'>

# Boolean
d = True
print(type(d))  # Output: <class 'bool'>
```

### 3. Loops

Loops are used to execute a block of code repeatedly. Python supports `for` and `while` loops.

#### For Loop

A `for` loop is used to iterate over a sequence (like a list, tuple, or string).

```python
# Example of a for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
```

#### While Loop

A `while` loop is used to execute a block of code as long as a condition is true.

```python
# Example of a while loop
count = 0
while count < 5:
    print(count)
    count += 1
# Output:
# 0
# 1
# 2
# 3
# 4
```

### 4. Conditionals

Conditionals are used to execute code based on certain conditions. The `if`, `elif`, and `else` statements are used for this purpose.

```python
# Example of conditionals
age = 18

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult.")
else:
    print("You are an adult.")
# Output: You just became an adult.
```

### Putting It All Together

Here's a simple program that uses variables, data types, loops, and conditionals:

```python
# Variables and data types
name = "Alice"
age = 20
is_student = True

# Conditional
if is_student:
    status = "student"
else:
    status = "not a student"

# Loop
for i in range(3):
    print(f"{name} is {age} years old and is a {status}.")
# Output:
# Alice is 20 years old and is a student.
# Alice is 20 years old and is a student.
# Alice is 20 years old and is a student.
```

In this example:

- We define variables `name`, `age`, and `is_student`.
- We use a conditional to set the `status` variable based on whether `is_student` is `True` or `False`.
- We use a `for` loop to print a message three times.

This should give you a good starting point for understanding basic Python syntax. Happy coding!
