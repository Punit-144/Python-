list = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Punit"]
print(list)

list.append("Bat")
# Bat is appended in the list since they are mutable 
print(list)

l1 = [1, 45, 56,2,7,29]
l1.sort() # Sorts the list in ascending order
print(l1) 

l1.reverse()
print(l1) # Reverse the content of the list in decending order

l1.insert(4, 2456) # Helps you insert a object into a particular index
print(l1)

l1.pop(2) # Lets you delete an element at a particular index and returns its value
print(l1)

l1.remove(45) # Removes a particular value from list
print(l1)