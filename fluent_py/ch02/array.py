from array import array
from random import random

floats = array('d', (random() for i in range(10**5)))
floats[-1]
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp=open('floats.bin', 'rb')
floats2.fromfile(fp, 10**5)
fp.close()
floats2[-1]

# in-place sort
a = array.array(a.typecode, sorted(a))
from array import array

number = array('h', [-2,-1,0,1,2])
memv = memoryview(number)
len(memv)
memv[0]
memv_oct = memv.cast('B')
memv_oct.tolist()
memv_oct[5]=4
number
import numpy

a = numpy.arange(12)
a
type(a)
a.shape
a.shape=3,4
a
a[:, 1]
a.transpose()


from collections import deque

dq = deque(range(10), maxlen=10)
dq
dq.rotate(3)
dq
dq.rotate(-4)
dq
dq.appendleft(-1)
dq
dq.extend([11,22,33]) # pushes out left
dq
dq.extendleft([10,20,30,40]) #extendleft(iter) reversed
dq