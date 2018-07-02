x = 5

def f(y, z):
    result = x + y + z
    return result
    
print(f(1,2))
print(f(3,4))

# Vocabulary:
#   variables: global vs. local
#   statements vs. expressions
#   function definitions vs. function calls
#   parameters vs. arguments


#Test functions
'''
def onesDigit(n):
    return n%10
    
def testOnesDigit():
    print("Testing onesDigit()...", end="")
    assert(onesDigit(5) == 5)
    assert(onesDigit(123) == 3)
    assert(onesDigit(100) == 0)
    assert(onesDigit(999) == 9)
    assert(onesDigit(-123) ==  3) # add this
    print("Passed!")
    
testOnesDigit() #Passed! why is this bad? crashed!!

'''
#local variable scope
def f(x):
    print("In f, x =", x)
    x += 5
    return x

def g(x):
    return f(x*2) + f(x*3)
    
print(g(2))
    

#another example

def f(x):
    print("In f, x= ", x)
    x += 7
    return round(x / 3)


def g(x):
    x *= 10
    return 2 * f(x)
    
def h(x):
    x += 3
    return f(x+4) + g(x)

print(h(f(1)))    # h(3) f(10) g(6) 6+44


#global varibale is evil

# In general, you should avoid using global variables.
# You will even lose style points if you use them!
# Still, you need to understand how they work, since others
# will use them, and there may also be some very few occasions
# where you should use them, too!

g = 100

def f(x):
    # If we modify a global variable, we must declare it as global.
    # Otherwise, Python will assume it is a local variable.
    global g
    g += 1
    return x + g

print(f(5)) # 106
print(f(6)) # 108
print(g)    # 102

#arguments默认值

def f(x, y=10):
    return x + y
    
    
print(f(5))
print(f(5, 1))






