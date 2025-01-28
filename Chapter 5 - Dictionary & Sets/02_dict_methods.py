marks = {
    "Punit" : 100,
    "Harry" : 89,
    "Rohan" : 23
}

print(marks.items()) # Gives you output in key-value pairs in form of tuples

print(marks.keys()) # Gives you the keys 
print(marks.values()) # Gives you the value

marks.update({"Harry" : 90, "Arya": 95 })
print(marks)

"""
We could not write print(marks.update({key:value})) since update does not return anything,
instead it changes the dictionary so output here would've been "none". hence we print "marks" variable.
"""

print(marks.get("Punit"))

"""
If we would've given it a key which is not in dictionary like print(marks.get(Nal))
It would've returned the output as none since there was not any key by its name
"""

# Difference between the two methods:

print(marks.get("Punit")) # Prints None.
print(marks["Punit"]) # Returns an error