
import math
import webbrowser



def helloWorld():
    print("hello wolrd!")
    
helloWorld()


#print(1/0)

print("2+2=5")

print("Carpe")
print("diem")

print("Carpe ", end="")
print("diem")

print() # blank line

#Compute the hypotenuse of a right trigangle

a = 3
b = 4
c = ((a**2 + b**2))**0.5

print("side a = ", a)
print("side b = ", b)
print("hypttenuse c = ", c)

#Basic console input

#name = input("Enter ur name: ")
#print("Ur name is:", name)

# ''空串不能转换成0
#x = int(input("Enter a number: "))
#print("One half of", x , "=", x/2) # type



#Importing modules
print(math.factorial(20))

#list all fns in math module

print(dir(math))

input("Hit enter to see the online docs for the math module.")

webbrowser.open("https:www.baidu.com")





























