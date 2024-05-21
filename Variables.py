# Arithmetic_operators
# Python operators : Arithmétic operators Arithmetic operators perform the common mathematical operation on the numeric operands.
# The arithmetic operators return the type of result depends on the type of operands, as below.
# Addition +: Sum of two operands
x, y = 5, 6
print(x + y) # output: 11

# Subtraction -: Left operand minus right operand
print(x - y) # -1

# Multiplication *: Left operand multiply by right operand
print(x * y) # output: 30

# Exponentiation ** : Left operand raised to the power of right
x = 2
y = 3
print(2 ** 3) # output: 8

# Division /
x = 6
y = 3
print(x/ y) # output: 2.0

# Floor division // # Sends the quotient rounded down to the lower integer
x = 6
y = 5
print(x // y) # output: 1

# Modulus: Reminder of a/b % to see if a number is even. if x%y == 0, x is even
x = 11
y = 3
print(x % y) # output: 2 (x is not even)
x=16
y=4
print(x % y) # output 0 (x is even)

# Assignment operators. The assignment operators are used to assign values to variables. The following table lists all the arithmetic operators in Python:
# += # Increases the value of a variable by adding another value to it.
x = 5
x += 5
print(x) # output: 10

# -= # Subtracts a value from a variable and assigns the result to the same variable
x = 5
x -= 2
print(x) # output: 3

# *= # Mulptiply a value from a variable and assigns the result to the same variable
x = 2
x *= 3
print(x) # output: 6

# /= # Divide a value from a variable and assigns the result to the same variable
x = 6
x /= 3
print(x) # output: 2.0

# //= # Floor Divide and assigns the result to the same variable
x = 6
x //= 5
print(x) # output: 1

# %= # Modulo and assigns the result to the same variable
x = 11
x %= 3
print(x) # output: 2

#Boolean Operations
## Comparison operators. The comparison operators compare two operands and return a boolean either True or False. The following table lists comparison operators in Python.
# >, returns True if the left operand is higher than the right one.
x = 5
y = 6
print(x > y) # output: False 

# <, returns True if the left operand is lower than right one
x = 5
y = 6
print(x < y) # output: True

# ==, returns True if the operands are equal
x = 5
y = 6
print(x == y) # output: False

# !=, returns True if the operands are not equal
x = 5
y = 6
print(x != y) # output : True

# >=, returns True if the left operand is higher than or equal to the right one
x = 5
y = 6
print(x >= y) # output: False

# <=, returns True if the left operand is lower than or equal to the right one
x = 5
y = 6
print(x <= y) # output: True

## Logical operators.The logical operators are used to combine two boolean expressions. The logical operations are generally applicable to all objects, and support truth tests, identity tests, and boolean operations.
# and, return True if both are true
x = 5
y = 6
print( x > 1 and y < 10) # output: True

# or, returns True if at least one is true
x = 5
y = 6
print( x > 1 or y < 10) # output: True

# not, returns True if an expression evalutes to false and vice-versa
x = 5
print(not x > 1) # output: False

## Identity operators
# is, returns True if both are true
x = 5
y = 6
print(x is y) # output: False

# is not, returns True if at least one is true
x = 5
y = 6
print(x is not y) # output: True

## Membership Test Operators. The membership test operators in and not in test whether the sequence has a given item or not. For the string and bytes types, x in y is True if and only if x is a substring of y.
# in, Returns True if the sequence contains the specified item else returns False.
nums = [1, 2, 3, 4, 5]
print(1 in nums) # output: True
print(10 in nums) # output: False
print("str" in "string") # output: True

# not in, not operator.contains(a,b). Returns True if the sequence does not contains the specified item, else returns False.
nums = [1, 2, 3, 4, 5]
print(1 not in nums) # output: False
print(10 not in nums) # output: True
print("str" not in "string") # output: False

# Variable type
## Integer variable
x = 69
print("Type of x:", type(x)) # output: Type of x: <class 'int'>

## Float variable
x= 6.4584122
print("Type of x:", type(x)) # output: Type of x: <class 'float'>

## String variable
greet = "Hello!"
print("Type of greet:", type(greet)) # output: Type of greet: <class 'str'>

## Boolean variable
Name = True
print("Type of Name:", type(Name)) # output: Type of Name: <class 'bool'>

## if and else statment
x = 123
y = 789
z = x+y
print(z) # output: 912
if isinstance(z, int):
    print("yes it\'s an integer!")
else:
    print("it\'s not an integer!") # output: yes it's an integer!
