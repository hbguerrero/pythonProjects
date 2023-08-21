a = input("Enter a number: ")
a = int(a)
b = input("Enter b number: ")
b = float(b)
c = a + b

if a == b:
    print("equal")
else:
    print("Different")

print("Type of a is: ", type(a))
print("Type of b is: ", type(b))
print("c = ", c)

if type(a) == type(b):
    print("a and b are of the same type")
else:
    print("a and b are of different type")