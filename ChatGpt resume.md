WHAT IS PYTHON?
Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python is widely used in web development, data analysis, artificial intelligence, scientific computing, and more, thanks to its extensive libraries and community support.

MANDATORY TOOLS
To effectively work with Python, you'll need the following tools:

Python Interpreter: The core program that runs Python code. You can download it from the official Python website.
Integrated Development Environment (IDE): Tools like PyCharm, Visual Studio Code, or Jupyter Notebook enhance productivity.
Package Manager: Pip is the standard package manager for installing and managing Python packages.
KEYWORDS IN PYTHON
Python keywords are reserved words that have a special meaning and cannot be used as identifiers (variable names, function names, etc.). Examples include False, class, finally, is, return, None, continue, for, lambda, try, and True.

PYTHON VARIABLE
Variables in Python are used to store data. A variable is created the moment you first assign a value to it. For example:

python
Copier le code
x = 5
y = "Hello, World!"
PYTHON DATA TYPE
Python supports various data types including:

Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Text Type: str (string)
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
PYTHON OPERATORS
Arithmetic Operators
Used to perform mathematical operations:

+ (Addition)
- (Subtraction)
* (Multiplication)
/ (Division)
% (Modulus)
** (Exponentiation)
// (Floor Division)
Assignment Operators
Used to assign values to variables:

= (Assign)
+= (Add and assign)
-= (Subtract and assign)
*= (Multiply and assign)
/= (Divide and assign)
//= (Floor divide and assign)
**= (Exponentiate and assign)
%= (Modulus and assign)
Comparison Operators
Used to compare two values:

== (Equal)
!= (Not equal)
> (Greater than)
< (Less than)
>= (Greater than or equal to)
<= (Less than or equal to)
Logical Operators
Used to combine conditional statements:

and (Logical AND)
or (Logical OR)
not (Logical NOT)
Identity Operators
Used to compare objects to check if they are the same:

is
is not
STRINGS
String Methods
Python provides a variety of methods for string manipulation, such as:

upper()
lower()
strip()
replace()
split()
String Formatting
Allows the inclusion of variables within strings:

python
Copier le code
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
String Indexing and String Slicing
Indexing: Accessing individual characters in a string.
Slicing: Accessing a substring. For example:
python
Copier le code
s = "Hello, World!"
print(s[0])  # H
print(s[0:5])  # Hello
String Length
Obtaining the length of a string using len() function:

python
Copier le code
s = "Hello, World!"
print(len(s))  # 13
String Multiplication
Repeating a string multiple times:

python
Copier le code
s = "Hello"
print(s * 3)  # HelloHelloHello
Character Escaping
Using backslashes to escape characters:

python
Copier le code
s = "He said, \"Hello!\""
print(s)  # He said, "Hello!"
f-String
Formatted string literals, prefixed with f or F:

python
Copier le code
name = "Alice"
print(f"Hello, {name}!")
String Operators
Concatenation: +
Repetition: *
Membership: in, not in
Regular Expression
A powerful tool for string matching and manipulation:

python
Copier le code
import re
pattern = r'\bfoo\b'
text = "foo bar baz"
match = re.search(pattern, text)
LOOP
while loop syntax
Executes as long as the condition is true:

python
Copier le code
i = 0
while i < 5:
    print(i)
    i += 1
While Loop with else Block
The else block executes when the loop condition is false:

python
Copier le code
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("i is no longer less than 5")
for loop
Iterates over a sequence (like a list, tuple, string):

python
Copier le code
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
PYTHON FUNCTIONS
Math Functions
Basic mathematical functions provided by Python:

abs()
max()
min()
round()
Advanced Math Functions
Available through the math module:

math.sqrt()
math.sin()
math.cos()
math.log()
Each of these topics provides a foundational understanding of Python and its capabilities.
