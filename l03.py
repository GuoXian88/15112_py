#builtin types. primitive data type


import math

def f():
    print("This is a user-defined function")
    return 42
    
print("Some basic types in Python: ")
print(type(2))
print(type(2.2))
print(type("2.2"))
print(type(2 < 2.2))

print(type(math))
print(type(math.tan))
print(type(f))
print(type(type(42)))



print("##################################")

print("And some other types we will see later in the course...")
print(type(Exception()))
print(type(range(5)))
print(type([1,2,3]))
print(type((1,2,3)))
print(type({1,2}))
print(type({1:42}))
print(type(2+3j))


print("Some builtin constants:")
print(True)
print(False)
print(None)

print("And some more constants in the math module:")
print(bool(0))
print(float(42))
print(int(2.8)) #floor in math?


print("And some basic math functions: ")
print(abs(-5))
print(max(2,3))
print(min(2,3))
print(pow(2,3))
print(round(2.354, 1)) #round with given number of digits


def shifY(y, digits):
    y <<= digits
    return y
    

print("shiftY called: ", shifY(1,2))
print(1^12) # binary bit xor 1100 ^ 0001 1101 --> 13

print(3 * 2)
print(3 * "abc")
print("abc"+ "def")
#print(3 + "def") # TypeError
print(str(3) + "def")


#integer division

print("The / operator does 'normal' float division: ")

print(" 5/3 = ", (5/3))
print()
print("The // operator does integer division: ")
print(" 5//4 =", (5//3))
print(" 2//3 = ", (2//3))
print(" -1//3 = ", (-1//3)) # //是往左边走的
print(" -4//3 =", (-4//3))

#modulus and remainder operator

print(" 6%3 = ", (6%3))
print(" 5%3 = ", (5%3))
print(" 2%3 = ", (2%3))
print(" 0%3 = ", (0%3))
print(" -4%3 = ", (-4%3))



