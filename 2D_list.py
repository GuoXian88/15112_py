#2d list
# create a 2d list with fixed values (static allocation)
a = [ [ 2, 3, 4 ] , [ 5, 6, 7 ] ]
print(a)


#shallow copy
# Try, and FAIL, to create a variable-sized 2d list
rows = 3
cols = 2

a = [ [0] * cols ] * rows # Error: creates shallow copy
                          # Creates one unique row, the rest are aliases!
 
print("This SEEMS ok.  At first:")
print("   a =", a)

a[0][0] = 42
print("But see what happens after a[0][0]=42")
print("   a =", a)



# Create a variable-sized 2d list
rows = 3
cols = 2

a=[]
for row in range(rows): a += [[0]*cols]

print("This IS ok.  At first:")
print("   a =", a)

a[0][0] = 42
print("And now see what happens after a[0][0]=42")
print("   a =", a)


def make2dList(rows, cols):
    a=[]
    for row in range(rows): a += [[0]*cols]
    return a

rows = 3
cols = 2

a = make2dList(rows, cols)

print("This IS ok.  At first:")
print("   a =", a)

a[0][0] = 42
print("And now see what happens after a[0][0]=42")
print("   a =", a)

#good to use list comprehension
rows = 3
cols = 2

a = [ ([0] * cols) for row in range(rows) ]

print("This IS ok.  At first:")
print("   a =", a)

a[0][0] = 42
print("And now see what happens after a[0][0]=42")
print("   a =", a)



import copy

# Create a 2d list
a = [ [ 1, 2, 3 ] , [ 4, 5, 6 ] ]

# Try to copy it
b = copy.copy(a) # Error:  creates shallow copy

# At first, things seem ok
print("At first...")
print("   a =", a)
print("   b =", b)

# Now modify a[0][0]
a[0][0] = 9
print("But after a[0][0] = 9")
print("   a =", a)
print("   b =", b)

#deepCopy的问题
a = [[0]*2]*3 # makes 3 shallow copies of (aliases of) the same row
a[0][0] = 42  # appears to modify all 3 rows
print(a)      # prints [[42, 0], [42, 0], [42, 0]]

# now do it again with a deepcopy

import copy
a = [[0]*2]*3        # makes 3 shallow copies of the same row
a = copy.deepcopy(a) # meant to make each row distinct
a[0][0] = 42         # so we hope this only modifies first row
print(a)             # STILL prints [[42, 0], [42, 0], [42, 0]]

# now one more time with a simple deepcopy alternative that does
# what we thought deepcopy did...

def myDeepCopy(a):
    if (isinstance(a, list) or isinstance(a, tuple)):
        return [myDeepCopy(element) for element in a]
    else:
        return copy.copy(a)

a = [[0]*2]*3     # makes 3 shallow copies of the same row
a = myDeepCopy(a) # once again, meant to make each row distinct
a[0][0] = 42      # so we hope this only modifies first row
print(a)          # finally, prints [[42, 0], [0, 0], [0, 0]]

# what's going on with deepcopy? Answer: if the original list has aliases,
# the deepcopied list will have aliases (of a single copy, not the original).
# So copy.deepcopy preserves alias structure!

# copy (not an alias!); expensive (new list created)
a = [ [ 1, 2, 3 ] , [ 4, 5, 6 ] ]
col = 1
colList = [ ]
for i in range(len(a)):
    colList += [ a[i][col] ]
print(colList)

