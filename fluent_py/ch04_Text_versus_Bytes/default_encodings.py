# code point 是一个数字 0-1114111
# 表示一个字符的 acutal bytes依赖于使用的编码
# 编码：一种code points  (decoding)<->(encoding) byte sequences 互相转换算法


s = 'cafe😶'
len(s) # 5
b = s.encode('utf8')
b # b'cafe\xf0\x9f\x98\xb6'   byte sequence starts with b prefix cafe是ascii另外一个不是，用16进制表示
len(b) # 8
b.decode('utf8') #'cafe😶'

# bytes and bytearray 0-255  \x00是null byte

bytes.fromhex('31 4B CE A9') # b'1K\xce\xa9'

import array
numbers = array.array('h', [-2,-1,0,1,2]) # array with short integers
octets = bytes(numbers)
octets # b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00'

#structs and memory views

import struct

fmt = '<3s3sHH'  # <小端 3s3s：2个3bytes的sequences HH:2个16bit整数
with open('sleep.jpg', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
bytes(header)  # b'\xff\xd8\xff\xe0\x00\x10JFIF'
struct.unpack(fmt, header)  # (b'\xff\xd8\xff', b'\xe0\x00\x10', 17994, 17993) type version width height
del header  # release memory associated with the memoryview instances
del img



# discover encoding of a byte sequence


import sys, locale

expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """

my_file = open('dummy', 'w')

for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))

'''
locale.getpreferredencoding() -> 'cp936'
                 type(my_file) -> <class '_io.TextIOWrapper'>
              my_file.encoding -> 'cp936'
           sys.stdout.isatty() -> False
           sys.stdout.encoding -> 'UTF-8'
            sys.stdin.isatty() -> False
            sys.stdin.encoding -> 'cp936'
           sys.stderr.isatty() -> False
           sys.stderr.encoding -> 'UTF-8'
      sys.getdefaultencoding() -> 'utf-8'
   sys.getfilesystemencoding() -> 'utf-8'
'''



