from array import array
import math

# BEGIN VECTOR2D_V3_PROP
class Vector2d:
    typecode = 'd' #If you want to change a class attribute you must set it on
    # the class directly, not through an instance.

    def __init__(self, x, y):
        self.__x = float(x)  # <1> private member __v
        self.__y = float(y)

    @property  # <2> getter method
    def x(self):  # <3>
        return self.__x  # <4>

    @property  # <5>
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))  # <6>

    # remaining methods follow (omitted in book listing)
# END VECTOR2D_V3_PROP

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

# BEGIN VECTOR_V3_HASH
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
# END VECTOR_V3_HASH

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)