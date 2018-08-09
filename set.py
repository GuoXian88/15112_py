#set
s = set([2,3,5])
print(3 in s)          # prints True
print(4 in s)          # prints False
for x in range(7):
    if (x not in s):
        print(x)       # prints 0 1 4 6
        
s = set()
print(s)     # prints set()

s = set("wahoo")
print(s)     # surprised?

s = { }
print(type(s) == set)  # False!
print(type(s))         # This is a dict (we'll learn about those soon)

#无序
s = set([2,4,8])
print(s)          # prints {8, 2, 4} in standard Python (though not in brython)
for element in s: # prints 8, 2, 4
    print(element)