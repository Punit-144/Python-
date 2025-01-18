a = 31
t = type(a) 
print(t)
# Output will be class <int>

b = 31.6
u = type(b) 
print(u)
# Output will be class <float>

c = "Punit"
y = type(c)
print(y)
# Ouput will be class <String>
 
d = "56.87"
i = type(d)
print(i)
# Ouput will be class <String>

e = "76.3"
f = float(e) # f but the type should be float
t = type(b)

print(t)

# Output will be float (TypeConversion)