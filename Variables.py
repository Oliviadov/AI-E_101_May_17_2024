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
# >, return True if the left operand is higher than the right one.
x = 5
y = 6
print(x > y) # output: False 

# <, return True if the left operand is lower than right one
x = 5
y = 6
print(x < y) # output: True

# ==, return True if the operands are equal
x = 5
y = 6
print(x == y) # output: False

# !=, return True if the operands are not equal
x = 5
y = 6
print(x != y) # output : True

# >=, return True if the left operand is higher than or equal to the right one
x = 5
y = 6
print(x >= y) # output: False

# <=, return True if the left operand is lower than or equal to the right one
x = 5
y = 6
print(x <= y) # output: True

# Logical operators.The logical operators are used to combine two boolean expressions. The logical operations are generally applicable to all objects, and support truth tests, identity tests, and boolean operations.
# and, return True if both are true
x = 5
y = 6
print( x > 1 and y < 10) # output: True

# or, return True if at least one is true
x = 5
y = 6
print( x > 1 or y < 10) # output: True

# not, Returns True if an expression evalutes to false and vice-versa
x = 5
print(not x > 1) # output: False

# Identity operators
# is, return True if both are true
x = 5
y = 6
print(x is y) # output: False

# is not, return True if at least one is true
x = 5
y = 6
print(x is not y) # output: True
