#builtin types. primitive data type


import math
import numbers

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
print(" -4%3 = ", (-4%3)) # 2
# print(" 3%0 = ", (3%0)) #error


#Verify that (a%b) is equivalent to (a - (a//b)*b)
def mod(a, b):
    return a - (a//b)*b
print(41%14, mod(41,14))
print(14%41, mod(14,41))
print(-32%9, mod(-32,9))
print(32%-9, mod(32,-9))

#优先级

print("Precedence：")

print(2+3*4)
print(5+4%3)
print(2**3*4)
print()

print("Associativity:")
print(5-4-3)
print(4**3**2) #right to left


#float number
print(0.1 + 0.1 == 0.2)        # True, but...
print(0.1 + 0.1 + 0.1 == 0.3)  # False!
print(0.1 + 0.1 + 0.1)         # prints 0.30000000000000004 (uh oh)
print((0.1 + 0.1 + 0.1) - 0.3) # prints 5.55111512313e-17 (tiny, but non-zero!)


#Short-Circuit Evaluation 'and or'


def isPositive(n):
    result = (n>0)
    print("isPositive(", n, ") = ", result)
    return result

def isEven(n):
    result = ( n % 2 == 0)
    print("isEven(",n,") =",result)
    return result


print("Test 1: isEven(-4) and isPositive(-4))")
print(isEven(-4) and isPositive(-4)) # Calls both functions
print("----------")
print("Test 2: isEven(-3) and isPositive(-3)")
print(isEven(-3) and isPositive(-3)) # Calls only one function!

#type vs isinstance

# In general, you should use (isinstance(x, T)) instead of (type(x) == T)

print(type("abc") == str)
print(isinstance("abc", str))


# We'll see better reasons for this when we cover OOP + inheritance later
# in the course.  For now, here is one reason:  say you wanted to check
# if a value is any kind of number (int, float, complex, etc). 
# You could do:

def isNumber(x):
    return (type(x) == int) or (type(x) == float)
    
print(isNumber(1), isNumber(1.1), isNumber(1+2j), isNumber("wow"))

# god damn good isNumberFromLib
# 有点像js的instanceof检查原型链?

def isNumberFromLib(x):
    return isinstance(x, numbers.Number) #works for any kind of number
    
print(isNumberFromLib(1), isNumberFromLib(1.1), isNumberFromLib(1+2j), isNumberFromLib("wow"))    




