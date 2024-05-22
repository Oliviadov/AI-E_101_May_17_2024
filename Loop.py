# While Loop
num = 0
while num < 5:
    num += 1   # num += 1 is same as num = num + 1
    print('Num = ', num) 
    if num == 3:  # condition before exiting a loop
        break     # Exit while loop.
# output: Num =  1; Num =  2; Num =  3

zoo = ["lion", "tiger", "elephant", "giraffe", "python"]
while True:    # This condition cannot possibly be false
    animal = zoo.pop()  # Extract one element from the end of the list
    print(animal)
    if animal == "elephant":
       break
print(zoo)
# output: python giraffe elephant. ['lion', 'tiger']

# Continue next iteration
num = 1
while num < 2:
    num += 1   # num += 1 is same as num = num + 1
    if num > 5: # condition before exiting a loop
        continue
    print('Num = ', num) # output: Num =  2

# For loop with the list object
nums = [5, 10, 15, 20, 25]
for i in nums:
    print(i) # output: 5 10 15 20 25
  
# for loop with a tuple object
nums = (1, 2, 3, 4, 5, 6, 7, 8)
for i in nums:
    print(i) # output: 1 2 3 4 5 6 7 8

# For Loop with String
for char in "Famous":
    print(char) # output: F a m o u s

# For Loop with Dictionary
nums = {1: 'Clhoe', 2: 'Lumen', 3: 'Zoe''}
for pair in nums.items():
    print(pair) # output: (1, 'Clhoe') (2, 'Lumen') (3, 'Zoe')
# To get the output separately
nums = {1: 'Clhoe', 2: 'Lumen', 3: 'Zoe'}
for x, y in nums.items():
    print("X =", x, "Y =", y) # output: X = 1 Y = Clhoe; X = 2 Y = Lumen; X = 3 Y = Zoe

# For Loop with the range() Function
for i in range(1, 10):
    if i >= 3:
        continue
    print(i) # output: 1, 2
# For Loop with Else Block
for i in range(8):
    print(i)
else:
    print('End of for loop') # 0 1 2 3 4 5 6 7 8; End of for loop

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equal', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number') # output: 2 is a prime number; 3 is a prime number; 4 equal 2 * 2; 5 is a prime number; 6 equal 2 * 3; 7 is a prime number; 8 equal 2 * 4; 9 equal 3 * 3
