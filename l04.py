

def f(x):
    print("A", end="")
    if(x == 0):
        print("B", end="")
        print("C", end="")
    print("D")
    
    
f(0)
f(1)


def abs1(n):
    if (n < 0):
        n = -n
    return n
    
def abs2(n):
    if (n < 0): n = -n
    return n
    
def abs3(n):
    if(n < 0):
        return -n
    return n

def abs4(n):
    return (n < 0)*(-n) + (n >= 0)*(n)
    
print("abs1(5) =", abs1(5), "and abs1(-5) =", abs1(-5))
print("abs2(5) =", abs2(5), "and abs2(-5) =", abs2(-5))
print("abs3(5) =", abs3(5), "and abs3(-5) =", abs3(-5))
print("abs4(5) =", abs4(5), "and abs4(-5) =", abs4(-5))


#loop
'''
def sumFromMToN(m, n):
    total = 0
    for x in range(m, n+1):
        total += x
    return total

print(sumFromMToN(5, 10))
print(sumFromMToN(5, 10) == 5+6+7+8+9+10)
'''
def sumFromMToN(m, n):
    return sum(range(m, n+1))
    
def sumToN(n):
    return n*(n+1)//2
    
def sumFromMToN_byFormula(m, n):
    return (sumToN(n) - sumToN(m - 1))
    
print(sumFromMToN_byFormula(5, 10) == 5+6+7+8+9+10)

def sumEveryKthFromMToN(m, n, k):
    total = 0
    for x in range(m, n+1, k):
        total += x
    return total

print(sumEveryKthFromMToN(5, 20, 7) == (5 + 12 + 19))


def printCoordinates(xMax, yMax):
    for x in range(xMax+1):
        for y in range(yMax+1):
            print("(", x, ",", y, ")  ", end="")
        print()

printCoordinates(4, 5)


def printStarRectangle(n):
    # print an nxn rectangle of asterisks
    for row in range(n):
        for col in range(n):
            print("*", end="")
        print()

printStarRectangle(5)

def printMysteryStarShape(n):
    for row in range(n):
        print(row, end=" ")
        for col in range(row):
            print("*", end=" ")
        print()

printMysteryStarShape(5)

for n in range(200):
    if (n % 3 == 0):
        continue # skips rest of this pass (rarely a good idea to use "continue")
    elif (n == 8):
        break # skips rest of entire loop
    print(n, end=" ")
print()


def readUntilDone():
    linesEntered = 0
    while(True):
        response = input("Enter a string (or 'done' to quit): ")
        if (response == "done"):
            break
        print(" You entered: ", response)
        linesEntered += 1
    print("Bye!")
    return linesEntered
    
#linesEntered = readUntilDone()

#print("You entered", linesEntered, "lines (not counting 'done').")

#Note: this is still not the fastest way, but it's a nice improvement.
def fasterIsPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

# And try out this version:
for n in range(100):
    if fasterIsPrime(n):
        print(n, end=" ")
print()
    


def nthPrime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (fasterIsPrime(guess)):
            found += 1
    return guess

# and let's see a list of the primes
for n in range(10):
    print(n, nthPrime(n))
print("Done!")


