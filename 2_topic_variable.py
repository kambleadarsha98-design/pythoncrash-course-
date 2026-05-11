# 2. Variables & Simple Data Types
# LOGIC	Variables are labelled boxes. You put a value in a box, give the box a name, and use that name later. Python figures out the type automatically.

# Variables
# A variable stores a value. You create it by writing:  name = value
# message = 'Hello'       # stores text
# age = 25                # stores a number
# price = 9.99            # stores a decimal

# print(message)          # Output: Hello
# print(age)              # Output: 25

# RULE	Variable names: lowercase, no spaces (use underscore), cannot start with a number.   Good: my_name   Bad: 2name, my name

# Strings
# A string is text inside quotes. You can use single or double quotes.
# name = 'kamble'
# print(name.title())      # Output: Kamble   (capitalize each word)
# print(name.upper())      # Output: KAMBLE
# print(name.lower())      # Output: kamble

# # Combining strings (concatenation)
# first = 'Hello'
# second = 'World'
# print(first + ' ' + second)  # Output: Hello World

# # f-string (modern, cleaner way)
# print(f"My name is {name}")  # Output: My name is kamble

# Numbers
# Python handles two kinds of numbers: integers (whole) and floats (decimal).
# # Integers
# x = 10
# y = 3
# print(x + y)    # 13  (addition)
# print(x - y)    # 7   (subtraction)
# print(x * y)    # 30  (multiplication)
# print(x / y)    # 3.333  (division — always returns float)
# print(x // y)   # 3   (floor division — no decimal)
# print(x % y)    # 1   (remainder / modulo)
# print(x ** y)   # 1000  (power: 10³)

# # Floats
# pi = 3.14159
# print(round(pi, 2))   # 3.14

# Type	Example	Key Methods / Notes
# String (str)	"Hello"  or  'Hello'	.upper()  .lower()  .title()  .strip()  len()
# Integer (int)	10, -5, 0	+ - * // % **  (no decimal point)
# Float (float)	3.14, -0.5	Has decimal point. Division always returns float
#  
