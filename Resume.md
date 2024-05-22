### WHAT IS PYTHON?
Python is a high-level, cross-platform, and open-sourced programming language released under a GPL-compatible license. He has become the language of choice for Data Science, Machine Learning, Web Developement, Image Processing, Game Developement, and Artificial Intelligence.
### MANDATORY TOOLS 
Before to start coding and programming with Python, some mandatory tools need to install, including:
• Python Miniconda with python 3.10, https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe/;
• Jupyter Notebook, https://jupyter.org/; 
• ChatGPT, https://chat.openai.com/; 
• PyCharm Community Edition, https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC/;
• Git, https://github.com/git-for-windows/git/releases/download/v2.44.0.windows.1/Git-2.44.0-64-bit.exe.
### KEYWORD IN PYTHON
A computer programming language is made up of a set of predefined words called keywords. A prescribed usage rule for each keyword is called syntax. 
Here is some list of the Python keywords: (False, None, True, and, as, else, elif, if, in, is, while, etc). The global list of Python keywords can be obtained using the following help command. eg: help("keywords"). Enter any keyword to get more help. eg: help("while"). # NB: Except for the first three (False, None and True), the other keywords are entirely in lowercase.
### PYTHON VARIABLE
In Python, a variable is a container that stores a value. In other words, variable is the name given to a value, so that it becomes easy to refer to it later. eg: x = "Hello Olivia!" ; print(x). I'll have the output: Hello Olivia! # Explanation: Here the name of my variable is x and her value is "Hello Olivia!.
Variable names may only contain Latin letters, digits, and/or the underscore character, and they cannot start with a digit. They also cannot be any of the reserved keywords. Variable names must start with a letter and can contain only letters, '_', and numbers.
### PYTHON DATA TYPE
Data types are the classification or categorization of data items. 
We distinguish: (i) Scalar Types, including: *int: Positive or negative whole numbers (without a decimal part) eg: -10, 10, 4, 5, 3554714; *float: Any real number with a decimal part. eg: 1.53, 8.455; *bool: Data with one of two built-in values True or False; *None: The None represents the null object in Python. A None is returned by functions that don't explicitly return a value; *complex: A number with a real and imaginary component represented as x + 3y.
(ii) Sequence Type, including: *String: A string value is a collection of one or more characters put in single('), double(") or triple quotes(''').; *List: A list object is an ordered collection of one or more data items, not necessarily of the same type, put in square brackets []; *Tuple: A Tuple object is an ordered collection of one or more data items, not necessarily of the same type, put in parentheses().
(iii) Mapping Type: *Dictionary: A dictionary Dict() object is an unordered collection of data in a key:value pair form. A collection of such pairs is enclosed in curly brackets. For example: {1:"Brian", 2:"Bill", 3:"Ram", 4: "Lucas"}.
#### NB: Numbers, strings, and Tuples are immutable, which means their contents can't be altered after creation. On the other hand, items in a List or Dictionary object can be modified. It is possible to add, delete, insert, and rearrange items in a list or dictionary.
### PYTHON OPERATORS
Operators are special symbols that perform some operation on operands and returns the result. Python includes the following categories of operators:
### Arithmetic Operators
Arithmetic operators are used to perform mathematical operations on numeric operands. Python supports a variety of arithmetic operators, including: addition (+), subtraction(-), multiplication(*), division(/), exponentiation(**), floor division(//), modulus(%).
### Assignment Operators
The assignment operators are used to assign values to variables. Here are the common assignment operators: = (assign); += (Add and assign); -= (Subtract and assign) ; *= (Multiply and assign); /= (Divide and assign); %= (Modulo and assign); **= (Exponentiate and assign); //= (Floor divide and assign).
### Comparison Operators
The comparison operators <, >, <=, >=, ==, !=, compare two operands and return a boolean either True or False. 
### Logical Operators
The logical operators "and", "or", "not" are used to combine two boolean expressions. The logical operations are generally applicable to all objects, and support truth tests, identity tests, and boolean operations. 
### Identity Operators
The identity operators "is" and "is not" check whether the two objects have the same id value.
### STRINGS
String is an sequence of unicode characters wrapped inside single, double, or triple quotes. Strings can include letters, numbers, symbols, and even whitespace characters. eg: "Hello, Olivia!" 'Hello, World!' "3548".
### String methode
In Python, we have many useful string methods. Here is some of them: 
- string.replace() is used to returns a copy of the string where all occurrences of a substring are replaced with another substring;
- string.lower()	who returns the copy of the original string where in all the characters are converted to lowercase;
- string.upper()	who returns a string in the upper case. Symbols and numbers remain unaffected;
- string.split()	who splits the string from the specified separator and returns a list object with string elements;
- string.strip()	who returns a copy of the string by removing both the leading and the trailing characters;
- string.find()	who returns the index of the first occurence of a substring in the given string (case-sensitive). If the substring is not found it returns -1;
- string.index()	who returns the index of the first occurence of a substring in the given string.
### String formatting
f-strings support various formatting options to control the appearance of values within the string. eg: x = 6.454534547865; formatted_x = f"{x:.4f}"; print("Formatted_x:", formatted_x). The output will return Formatted_x: 6.4545. Explanation: :".4f" specifies that the value of x should be formatted as a floating-point number with 4 decimal places.
### String indexing and string slicing
In Python string indexing allows to access individual characters in a string by their position, or index, within the string. Indexing in Python starts at 0 for the first character, and negative indices count backward from the end of the string. However, it's also possible to use slicing to extract substrings from a string.
eg: name = "Olivia" 
# Access the first character (index 0)
first_char = name[0]; print("First character:", first_char). The output will return "O".
# Access the last character (index -1)
last_char = name[-1]; print("Last character:", last_char). The output will return "a".
# Extract substrings from a string
substring = name[1:5]; print("Substring:", substring). The output will return "livi" 
###  String length
The len() function in Python is a built-in function that returns the length of an object. When applied to a string, it returns the number of characters in that string. 
eg: text = "Your father is famous"
# Get the lenght of the string
lenght = len(text)
print("Lenght of the string:", lenght). # output : 21. Spaces are taken into account
### String multiplication
The multiplication operator repeats a string a specified number of times. eg: text = "'78565\'"; result = text * 5; print(result). The output will return:'78565''78565''78565''78565''78565'.
### Character escaping
In Python, the escape character is used to invoke an alternative implementation of the subsequent character in a sequence. Backslash \ is used as an escape character. Here is somes of escape character common used: \\ Backslash; \' Single quote;\'' Double quote;\b	Backspace; \f	Form feed; \n	Newline; \nnn	Octal notation, where n is in the range 0-7; \t	Tab.
### f-String
A formatted string literal, or an f-string, is a string literal that is prefixed with 'f' or 'F'. It provide a convenient and concise way to embed expressions (such as variable names) within strings delimited by curly braces {}. eg: types_of_people = 10 ; x = f"There are {types_of_people} types of people." The output will return: There are 10 types of people.
### String Operators
In Python, arithmetic operators don't operate on strings. However, there are special operators for string processing, including: (+)	Appends the second string to the first; (*)	Concatenates multiple copies of the same string; []	Returns the character at the given index; [:]	Fetches the characters in the range specified by two index operands separated by the : symbol; (in)	Returns true if a character exists in the given string; (not in)	Returns true if a character does not exist in the given string.
### Regular Expression
Regular Expression, also known as Regex, is a tool for searching, modifying, and validating strings or text data. Regex allows you to search for specific character patterns, such as phone numbers, email addresses, dates, or any other format in text data. It can also be used to extract data from text or replace certain patterns with other text. It is possible to specify the exact pattern one wants to match, search for it in a string or text file, and replace it with the specific text. For example, you can search for the word "Hello" and replace it with "Hi" or search for the phone number in the format xx-xxxx-xxxx and replace it with the format xxx-xxx-xxxx. Regex can also be used to validate user input before processing it further. By validating user input, developers can ensure that processed data meets certain criteria, such as format, length, or type. Generally, pythex (https://pythex.org/) is used for testing regular expressions.
### L00P
In Python while and for keywords are used to constitute a conditional loop, by which repeated execution of a block of statements is done until the specified boolean expression is true.
### while loop synthax
Python keyword while has a conditional expression followed by the : symbol to start a block with an increased indent. This block has statements to be executed repeatedly. Such a block is usually referred to as the body of the loop. The body will keep executing till the condition evaluates to True. If and when it turns out to be False, the program will exit the loop. The break keyword is used to exit the while loop at some condition. The if condition is used to determine when to exit from the while loop.
### While Loop with else Block
The else block can follow the while loop. The else block will be executed when the boolean expression of the while loop evaluates to False. 
### for loop 
The for loop is used for iterating over sequence types such as list, tuple, set, range, etc. It cannot be used to execute some code repeatedly.
#### NB: If a loop (for loop or while loop) contains another loop in its body block, we say that the two loops are nested. If the outer loop is designed to perform m iterations and the inner loop is designed to perform n repetitions, the body block of the inner loop will get executed m X n times.
### PYTHON FUNCTIONS
A function is a reusable block of programming instructions designed to perform a certain task. Python includes many integrated functions. However, it is possible to define a function if the one integrated in Python is not appropriate to serve a given objective. To define a function, Python provides the keyword def. The keyword def is followed by a suitable identifier as the name of the function and parentheses. eg: def sum (): One or more parameters may be optionally mentioned inside parentheses. The : symbol after parentheses starts an indented block.
### Math functions
The Python standard library provides a good number of built-in math functions for common operations.Here are math functions provided by Python:
- math.sqrt(): allows to calculate the square root of a number.
- math.pow(): allows to calculate the power of a number.
- math.exp(): allows to calculate the exponential of a number.
- math.log(): allows to calculate the natural logarithm (ln) of a number.
- math.sin(), math.cos(), math.tan(): allows to calculate the trigonometric values (sine, cosine, tangent) of an angle given in radians.
- math.degrees(), math.radians(): convert angles between degrees and radians.
- math.ceil(), math.floor(): round a number up or down, respectively.
- math.fabs(): allows to calculate the absolute value of a number.
To access each math function import it in your Python code like this: import math.
### Advanced math functions
Python provides also a library for scientific computing and numerical operations on large multidimensional arrays and matrices. This library is called NumPy (Numeric Python) and is often used for compute-intensive workloads in signal processing, image processing, simulation, modeling, optimization, machine learning and data science. 
To access NumPy and its functions, import it in your Python code like this: import numpy as np
