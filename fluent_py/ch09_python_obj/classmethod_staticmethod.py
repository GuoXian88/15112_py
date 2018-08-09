'''
to define a method that operates
on the class and not on instances. classmethod changes the way the method is called,
so it receives the class itself as the first argument, instead of an instance. Its most com‐
mon use is for alternative constructors

In contrast, the staticmethod decorator changes a method so that it receives no special
first argument. In essence, a static method is just like a plain function that happens to
live in a class body, instead of being defined at the module level.

Python stores instance attributes in a per-instance dict named __dict__.
By defining __slots__ in the class, you are telling the interpreter: “These are all the
instance attributes in this class.” Python then stores them in a tuple-like structure in
each instance, avoiding the memory overhead of the per-instance __dict__. This can
make a huge difference in memory usage if your have millions of instances active at the
same time.
'''
# eg1
brl = 1/2.43
'1 BRL = {rate:0.2f} USD'.format(rate=brl)
'1 BRL = {rate:5.3e} USD'.format(rate=brl)

format(42, 'b')
format(2/3, '.1%')



from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes(array(Vector2d.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

# BEGIN VECTOR2D_V2_FORMAT
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):  # <1>
            fmt_spec = fmt_spec[:-1]  # <2> remove p
            coords = (abs(self), self.angle())  # <3>
            outer_fmt = '<{}, {}>'  # <4>
        else:
            coords = self  # <5>
            outer_fmt = '({}, {})'  # <6>
        components = (format(c, fmt_spec) for c in coords)  # <7>
        return outer_fmt.format(*components)  # <8>
# END VECTOR2D_V2_FORMAT

    @classmethod
    def frombytes(cls, octets):
        memv = memoryview(octets).cast(cls.typecode)
        return cls(*memv)