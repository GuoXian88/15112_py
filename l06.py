print("Two standard ways to create an empty list:")
a = []
b = list()

print(type(a), len(a), a)
print(type(b), len(b), b)
print(a == b)


a = [ "hello" ]
b = [ 42 ]

print(type(a), len(a), a)
print(type(b), len(b), b)
print(a == b)

a = [2, 3, 5, 7]
b = list(range(5))
c = ["mixed types", True, 42]

print(type(a), len(a), a)
print(type(b), len(b), b)
print(type(c), len(c), c)

n = 10
a = [0] * n
b = list(range(n))

print(type(a), len(a), a)
print(type(b), len(b), b)


a = [ 2, 3, 5, 2 ]
print("a = ", a)
print("len =", len(a))
print("min =", min(a))
print("max =", max(a))
print("sum =", sum(a))

a = [2, 3, 5, 7, 11, 13]
print("a        =", a)

# Access non-negative indexes
print("a[0]     =", a[0])
print("a[2]     =", a[2])

# Access negative indexes
print("a[-1]    =", a[-1])
print("a[-3]    =", a[-3])

# Access slices a[start:end:step]
print("a[0:2]   =", a[0:2])
print("a[1:4]   =", a[1:4])
print("a[1:6:2] =", a[1:6:2])


# Create a list
a = [ 2, 3, 5, 7 ]

# Create an alias to the list
b = a

# We now have two references (aliases) to the SAME list
a[0] = 42
b[1] = 99
print(a)
print(b)


def f(a):
    a[0] = 42
a = [2, 3, 5, 7]
f(a)
print(a)

# Create a list
a = [ 2, 3, 5, 7 ]

# Create an alias to the list
b = a

# Create a different list with the same elements
c = [ 2, 3, 5, 7 ]

# a and b are references (aliases) to the SAME list
# c is a reference to a different but EQUAL list

print("initially:")
print("  a==b  :", a==b)
print("  a==c  :", a==c)
print("  a is b:", a is b)
print("  a is c:", a is c)

# Now changes to a also change b (the SAME list) but not c (a different list)
a[0] = 42
print("After changing a[0] to 42")
print("  a=",a)
print("  b=",b)
print("  c=",c)
print("  a==b  :", a==b)
print("  a==c  :", a==c)
print("  a is b:", a is b)
print("  a is c:", a is c)

a = [ 2, 3, 5, 2, 6, 2, 2, 7 ]
print("a      =", a)
print("2 in a =", (2 in a))
print("4 in a =", (4 in a))


a = [ 2, 3, 5, 2, 6, 2, 2, 7 ]
print("a          =", a)
print("2 not in a =", (2 not in a))
print("4 not in a =", (4 not in a))

#list.index(item, start)
a = [ 2, 3, 5, 2, 6, 2, 2, 7 ]
print("a            =", a)
print("a.index(6)   =", a.index(6))
print("a.index(2)   =", a.index(2))
print("a.index(2,1) =", a.index(2,1))
print("a.index(2,4) =", a.index(2,4))

a = [ 2, 3 ]
a.append(7)
print(a)

# list.extend(list2)
a = [ 2, 3 ]
a += [ 11, 13 ]
print(a)


a = [ 2, 3, 5, 7, 11 ]
a.insert(2, 42)  # at index 2, insert 42
print(a)


a = [ 2, 3 ]
b = a[:2] + [5] + a[2:]
print(a)
print(b)

print("Destructive:")
a = [ 2, 3 ]
b = a
a += [ 4 ] #这个a的指向地址没有变化
print(a)
print(b)

print("Non-Destructive:")
a = [ 2, 3 ]
b = a
a = a + [ 4 ] #a的指向地址发生了改变指向新的地址
print(a)
print(b)

#理解下面这个比较重要
c=[1,2,3]
d=c#这里是d也指向c的地址，但不会随着c重新指向的地址变化而变化
#即不是动态指向的，没有动态绑定到c上而是绑定到地址上
c=[4,5]
print(d,c)


a = [ 2, 3, 5, 3, 7, 6, 5, 11, 13 ]
print("a =", a)

a.remove(5)
print("After a.remove(5), a=", a)

a.remove(5)
print("After another a.remove(5), a=", a)


#pop
a = [ 2, 3, 4, 5, 6, 7, 8 ]
print("a =", a)

item = a.pop(3)
print("After item = a.pop(3)")
print("   item =", item)
print("   a =", a)

item = a.pop(3)
print("After another item = a.pop(3)")
print("   item =", item)
print("   a =", a)

# Remove last item with list.pop()
item = a.pop()
print("After item = a.pop()")
print("   item =", item)
print("   a =", a)

#slice
a = [ 2, 3, 4, 5, 6, 7, 8 ]
a[2:4] = [ ]
print("a =", a)

#delete
a = [ 2, 3, 4, 5, 6, 7, 8 ]
del a[2:4]
print("a =", a)

#Non-Destructive
a = [ 2, 3, 5, 3, 7, 5, 11, 13 ]
print("a =", a)

b = a[:2] + a[3:]
print("After b = a[:2] + a[3:]")
print("   a =", a)
print("   b =", b)

#swap
a = [ 2, 3, 5, 7 ]
print("a =", a)

a[0] = a[1]
a[1] = a[0]
print("After failed swap of a[0] and a[1]:")
print("   a=",a)


a = [ 2, 3, 5, 7 ]
print("a =", a)

temp = a[0]
a[0] = a[1]
a[1] = temp
print("After swapping a[0] and a[1]:")
print("   a=",a)



a = [ 2, 3, 5, 7 ]
print("a =", a)

a[0],a[1] = a[1],a[0]
print("After swapping a[0] and a[1]:")
print("   a=",a)


#loop backward
a = [ 2, 3, 5, 7 ]
print("And here are the items in reverse:")
for index in range(len(a)):
    revIndex = len(a)-1-index
    print("a[", revIndex, "] =", a[revIndex])

#Hazard: modifying while looping

a = [ 2, 3, 5, 3, 7 ]
print("a =", a)

# Failed attempt to remove all the 3's
'''
for index in range(len(a)):
    if (a[index] == 3):  # this eventually crashes!
        a.pop(index)

print("This line will not run!")
'''


# Create some lists
a = [ 2, 3, 5, 3, 7 ]
b = [ 2, 3, 5, 3, 7 ]   # same as a
c = [ 2, 3, 5, 3, 8 ]   # differs in last element
d = [ 2, 3, 5 ]         # prefix of a

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)

print("------------------")
print("a == b", (a == b)) #居然不是比较地址和js不一样
print("a == c", (a == c))
print("a != b", (a != b))
print("a != c", (a != c))

print("------------------")
print("a < c", (a < c))
print("a < d", (a < d))


#copy list
import copy

# Create a list
a = [ 2, 3 ]

# Try to copy it
b = a             # Error!  Not a copy, but an alias
c = copy.copy(a)  # Ok

# At first, things seem ok
print("At first...")
print("   a =", a)
print("   b =", b)
print("   c =", c)

# Now modify a[0]
a[0] = 42
print("But after a[0] = 42")
print("   a =", a)
print("   b =", b)
print("   c =", c)


import copy

a = [2, 3]
b = copy.copy(a)
c = a[:]
d = a + [ ]
e = list(a)
f = copy.deepcopy(a)
g = sorted(a)

a[0] = 42
print(a, b, c, d, e, f, g)


#Non-Destructively with sorted(list)
a = [ 7, 2, 5, 3, 5, 11, 7 ]
print("At first")
print("   a =", a)
b = sorted(a)
print("After b = sorted(a)")
print("   a =", a)
print("   b =", b)

#sorting with a key function
a = [ 10, 2, -5, 8, -3, 7, 1 ]
print(sorted(a))
print(sorted(a, key=abs))


#fill
def fill(a, value):
    for i in range(len(a)):
        a[i] = value

a = [1, 2, 3, 4, 5]
print("At first, a =", a)
fill(a, 42)
print("After fill(a, 42), a =", a)

import copy

def destructiveRemoveAll(a, value):
    while (value in a):
        a.remove(value)

def nonDestructiveRemoveAll(a, value):
    a = copy.copy(a)
    while (value in a):
        a.remove(value)
    return a

a = [ 1, 2, 3, 4, 3, 2, 1 ]
print("At first")
print("   a =", a)

destructiveRemoveAll(a, 2)
print("After destructiveRemoveAll(a, 2)")
print("   a =", a)

b = nonDestructiveRemoveAll(a, 3)
print("After b = nonDestructiveRemoveAll(a, 3)")
print("   a =", a)
print("   b =", b)


#Tuples(Immutable Lists)
t = (1, 2, 3)
print(type(t), len(t), t)

a = [1, 2, 3]
t = tuple(a)
print(type(t), len(t), t)

#Parallel (tuple) assignment
(x, y) = (1, 2)
print(x)
print(y)

(x, y) = (y, x)
print(x)
print(y)

#单个tuple语法
t = (42)
print(type(t), t*5)

t = (42,)
print(type(t), t*5)


#important List Comprehensions
a = [i for i in range(10)]
print(a)

a = [(i*100) for i in range(20) if i%5 == 0]
print(a)



# use list(s) to convert a string to a list of characters
a = list("wahoo!")
print(a)  # prints: ['w', 'a', 'h', 'o', 'o', '!']

# use s1.split(s2) to convert a string to a list of strings delimited by s2
a = "How are you doing today?".split(" ")
print(a) # prints ['How', 'are', 'you', 'doing', 'today?']

# use "".join(a) to convert a list of characters to a single string
s = "".join(a)
print(s)  # prints: wahoo!

# "".join(a) also works on a list of strings (not just single characters)
a = ["parsley", " ", "is", " ", "gharsley"] # by Ogden Nash!
s = "".join(a)
print(s)  # prints: parsley is gharsley

















