name  = "punit"

print(len(name)) # give you the length of the string.

print(name.endswith("it")) # tells whether the string ends with the given input or not, returns boolean values

print(name.startswith("pu")) # tells whether the stting starts with the given input or not, returns boolean value

print(name.capitalize()) # Capitalize the starting character of the string

First  = "Hello World"
index = First.find("World")
print(index) # output = 6
# This function finds a word and returns the index of first occurance of that word in the string.

First = "Hello World"
replaced_string = First.replace("World", "Python")
print(replaced_string) # output = "Hello Python"

# This function replaces the old word with the new word in the entire string.