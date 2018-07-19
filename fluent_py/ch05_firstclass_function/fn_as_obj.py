def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n-1)

factorial.__doc__

fact = factorial
map(fact, range(11))#<map at 0x7277128>
list(map(fact, range(11)))#[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

# fp highorder function map, reduce, filer, apply

from functools import reduce
from operator import add

reduce(add, range(100))
sum(range(100))


"""
# BEGIN BINGO_DEMO
>>> bingo = BingoCage(range(3))
>>> bingo.pick()
1
>>> bingo()
0
>>> callable(bingo)
True
# END BINGO_DEMO
"""

# BEGIN BINGO

import random

class BingoCage:

    def __init__(self, items):
        self._items = list(items)  # <1>
        random.shuffle(self._items)  # <2>

    def pick(self):  # <3>
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')  # <4>

    def __call__(self):  # <5>
        return self.pick()

# END BINGO

"""
# BEGIN TAG_DEMO
>>> tag('br')  # <1>
'<br />'
>>> tag('p', 'hello')  # <2>
'<p>hello</p>'
>>> print(tag('p', 'hello', 'world'))
<p>hello</p>
<p>world</p>
>>> tag('p', 'hello', id=33)  # <3>
'<p id="33">hello</p>'
>>> print(tag('p', 'hello', 'world', cls='sidebar'))  # <4>
<p class="sidebar">hello</p>
<p class="sidebar">world</p>
>>> tag(content='testing', name="img")  # <5>
'<img content="testing" />'
>>> my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
...           'src': 'sunset.jpg', 'cls': 'framed'}
>>> tag(**my_tag)  # <6>
'<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'
# END TAG_DEMO
"""


# BEGIN TAG_FUNC
def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)
# END TAG_FUNC


import bobo

@bobo.query('/')
def hello(person):
    return 'Hello %s!' % person



