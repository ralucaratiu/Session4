# Exceptions

# print(7/0)
# a = int("3")

# primt= print
# primt("salut")

try:
    r =  float(input("what is the radius? \n"))
    print("the surface of the circle is ", r**2*3.14)
except ValueError:
    print("next introduce a correct radius")