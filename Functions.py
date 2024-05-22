# Function Parameters
def greet(name):
    print('Hello ', name)
greet("Mirabelle) # calling function with argument
greet(2145)
# output : Hello  Mirabelle; Hello  2145

# Multiple Parameters      
def greet(name1, name2, name3):  
    print('Hello ', name1, ' , ', name2, ', and ', name3)
greet('Olivia', 'Bill', 'Natacha') # calling function with string argument
# output : Hello  Olivia  ,  Bill , and  Natacha
# Unknown Number of Arguments
def greet(*names): # Putting * before the parameter if you don't know the number of arguments the user is going to pass
    print('Hello ', names[0], ', ', names[1], ', ', names[2])
greet('Nathan', 'Octavio', 'Dilan') 
# output: Hello  Nathan ,  Octavio ,  Dilan

#Keyword Argument **kwarg
def greet(**person):
    print('Hello ', person['firstname'],  person['lastname'])
greet(firstname='Olivia', lastname='Dovoedo')
greet(firstname='Nicola', lastname='Tesla')
# output: Hello Olivia Dovoedo; Hello Nicola Tesla 

# Function with return value
def sum(a, b):
    return a + b
total = sum(10, 20) 
print(total)
total = sum(5, sum(10, 20))
print(total) # output: 30; 35
# Return Type
def sum(a, b) -> float: # -> is used to specify the type of return value
    return a + b
total = sum(10.5, 20.69)
print(total)
total = sum(5, sum(10.5, 20.69))
print(total) # 31.19; 36.19

# Lambda function
greet = lambda name: print('Hello ', name)
greet('Steve') # output: Hello  Steve

sum = lambda x, y, z : x + y + z
n = sum(5, 10, 15)
print(n) # output: 30

