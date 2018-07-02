#string

# single-quoted or double-quoted strings are the most common
print('single-quotes')
print("double-quotes")

# triple-qouted strings are less common (though see next section for a typical use)
print('''triple single-quotes''')
print("""triple double-quotes""")

print("abc\ndef")  # \n is a single newline character
print("""abc
def""")

print("""\
You can use a backslash at the end of a line in a string to exclude
the newline after it. This should almost never be used, but one good
use of it is in this example, at the start of a multi-line string, so
the whole string can be entered with the same indentation (none, that is).
""")

print("Double-quote: \"")
print("Backslash: \\")
print("Newline (in brackets): [\n]")
print("Tab (in brackets): [\t]")

print("These items are tab-delimited, 3-per-line:")
print("abc\tdef\tg\nhi\tj\\\tk\n---")



s = "a\\b\"c\td"
print("s =", s)
print("len(s) =", len(s))


import string
print(string.ascii_letters)   # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
print("-----------")
print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)          # 0123456789
print("-----------")
print(string.punctuation)     # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.printable)       # digits + letters + punctuation + whitespace
print("-----------")
print(string.whitespace)      # space + tab + linefeed + return + ...


print("ring" in "strings")
s = "abcdefgh"
print(s)
print(s[-1])
print(s[-2])


s = "abcdefgh"
print(s)
print(s[0:3])
print(s[1:3])
print("-----------")
print(s[2:3])
print(s[3:3])


s = "abcdefgh"
print(s)
print(s[3:])
print(s[:3])
print(s[:])

print("This is not as common, but perfectly ok.")
s = "abcdefgh"
print(s)
print(s[1:7:2])
print(s[1:7:3])


s = "abcdefgh"

print("This works, but is confusing:")
print(s[::-1])

print("This also works, but is still confusing:")
print("".join(reversed(s)))

print("Best way: write your own reverseString() function:")

def reverseString(s):
    return s[::-1]

print(reverseString(s)) # crystal clear!


s = "abcd"
for i in range(len(s)):
    print(i, s[i])
    
    
names = "fred,wilma,betty,barney"
for name in names.split(","):
    print(name)
    
# quotes from brainyquote.com
quotes = """\
Dijkstra: Simplicity is prerequisite for reliability.
Knuth: If you optimize everything, you will always be unhappy.
Dijkstra: Perfecting oneself is as much unlearning as it is learning.
Knuth: Beware of bugs in the above code; I have only proved it correct, not tried it.
Dijkstra: Computer science is no more about computers than astronomy is about telescopes.
"""
for line in quotes.splitlines():
    if (line.startswith("Knuth")):
        print(line)
        
# There are many ways to write isPalindrome(s)
# Here are several.  Which way is best?

def reverseString(s):
    return s[::-1]

def isPalindrome1(s):
    return (s == reverseString(s))

def isPalindrome2(s):
    for i in range(len(s)):
        if (s[i] != s[len(s)-1-i]):
            return False
    return True

def isPalindrome3(s):
    for i in range(len(s)):
        if (s[i] != s[-1-i]):
            return False
    return True

def isPalindrome4(s):
    while (len(s) > 1):
        if (s[0] != s[-1]):
            return False
        s = s[1:-1]
    return True

print(isPalindrome1("abcba"), isPalindrome1("abca"))
print(isPalindrome2("abcba"), isPalindrome2("abca"))
print(isPalindrome3("abcba"), isPalindrome3("abca"))
print(isPalindrome4("abcba"), isPalindrome4("abca"))

#strings are immutable

'''
name = input("Enter your name: ")
print("Hi, " + name + ". Your name has " + str(len(name)) + " letters!")
'''


print(ord("A")) # 65
print(chr(65))  # "A"
print(chr(ord("A")+1)) # ?


# eval() works but you should not use it!
s = "(3**2 + 4**2)**0.5"
print(eval(s))

def testfn():
    return 'testfn'
# why not? Well...
s = "testfn()"
print(eval(s))


# Run this code to see a table of isX() behaviors
def p(test):
    print("True     " if test else "False    ", end="")
def printRow(s):
    print(" " + s + "  ", end="")
    p(s.isalnum())
    p(s.isalpha())
    p(s.isdigit())
    p(s.islower())
    p(s.isspace())
    p(s.isupper())
    print()
def printTable():
    print("  s   isalnum  isalpha  isdigit  islower  isspace  isupper")
    for s in "ABCD,ABcd,abcd,ab12,1234,    ,AB?!".split(","):
        printRow(s)
printTable()


print("This is nice.  Really nice.".replace("nice", "sweet"))
print("This is nice.  Really nice.".replace("nice", "sweet", 1)) # count = 1


breed = "beagle"
print("Did you see a %s?" % breed)

dogs = 42
print("There are %d dogs." % dogs)

grade = 87.385
print("Your current grade is %0.1f!" % grade)

dogs = 42
cats = 18
exclamation = "Wow"
print("There are %d dogs and %d cats. %s!!!" % (dogs, cats, exclamation))

dogs = 42
cats = 3
print("%10s %10s" % ("dogs", "cats"))
print("%10d %10d" % (dogs, cats))

dogs = 42
cats = 3
print("%-10s %-10s" % ("dogs", "cats"))
print("%-10d %-10d" % (dogs, cats))


def readFile(path):
    with open(path, "rt") as f:
        return f.read()
        
def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)
        
contentsToWrite = "This is a test!\nIt is only a test!"
writeFile("foo.txt", contentsToWrite)

contentsRead = readFile("foo.txt")
assert(contentsRead == contentsToWrite)

print("Open the file foo.txt and verify its contents.")


