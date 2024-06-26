# Character_escaping
str1 = 'Welcome to \'Benin\' stadium'
print(str1) # output: Welcome to 'Benin' stadium
str2 = "Welcome to \"Benin\" stadium"
print(str2) # output: Welcome to "Benin" stadium

months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul"
print("Here are the months: ", months) # output: Here are the months: Jan Feb Mar Apr May Jun Jul

# fstring
name = 'Lee Y. Zlatan'
age = 40 # not a lie
waist = 74 # inches
weight = 160 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'
print(f"Let's talk about {name}.") # output: Let's talk about Lee Y. Zlatan.
print(f"He's {waist} inches tall.") # output: He's 74 inches tall.
print(f"He's {weight} pounds heavy.") # output: He's 160 pounds heavy.
print("Actually that's not too heavy.") # output: Actually that's not too heavy.
print(f"He's got {eyes} eyes and {hair} hair.") # output: He's got Brown eyes and Black hair.
print(f"His teeth are usually {teeth} depending on the coffee.") # output: His teeth are usually White depending on the coffee.

# Concatenation
end1 = "O"
end2 = "l"
end3 = "i"
end4 = "v"
end5 = "i"
end6 = "a"
end7 = "D"
end8 = "o"
end9 = "v"
end10 = "o"
end11 = "e"
end12 = "d"
end13 = "o"
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12 + end13) # output: Olivia Dovoedo

# String formatting
points = 5432
total = 1245
z = points/total
formatted_z = f"{z:.1%}"
print("Formatted_z:", formatted_z) # output: Formatted_z: 436.3%

# String indexing
name = "Murielle"
# Access,the first character (index 0)
first_char = name[0]
print("First character:", first_char) # output : "M"
# Access the last character (index -1)
last_char = name[-1]
print("Last character:", last_char) # output : e

# String slicing
# Extract substrings from a string
substring = name[2:6]
print("Substring:", substring) # output : "riel" 
# Acess a range of characteres using negative indexing
substring1 = name[-7:-4]
print("Substring1:", substring1) # output : "uri"

###  String length
text = "I have the best team!"
# Get the lenght of the string
lenght = len(text)
print("Lenght of the string:", lenght). # output : 21. Spaces are taken into account

# String multiplication
x = "'Amazing!\'"
y = x*10
print(y) # output :'Amazing!''Amazing!''Amazing!''Amazing!''Amazing!''Amazing!''Amazing!''Amazing!''Amazing!''Amazing!'




