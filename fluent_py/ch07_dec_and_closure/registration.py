# BEGIN REGISTRATION

registry = []  # <1>

def register(func):  # <2>
    print('running register(%s)' % func)  # <3>
    registry.append(func)  # <4>
    return func  # <5>

@register  # <6>
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():  # <7>
    print('running f3()')

def main():  # <8>
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__=='__main__':
    main()  # <9>




'''
running register(<function f1 at 0x00000000058C49D8>)
running register(<function f2 at 0x00000000058C4AE8>)
running main()
registry -> [<function f1 at 0x00000000058C49D8>, <function f2 at 0x00000000058C4AE8>]
running f1()
running f2()
running f3()
'''
# END REGISTRATION