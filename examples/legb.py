
"""
LEGB
L - locals
E - enclosing
G - global
B - builtins
"""

# Builtins

# print(name)
# print(len)
# from __builtins__ import *

# name = 'Dima'
# globals()['name'] = 'Dima'
# print(name)
len = 1

# print(globals())
# print(len)
print(__builtins__.len('HelloWorld'))

x = 2



class A:
    pass


def foo():
    x = 5
    print(f'Local foo: {x}')

    def bar():
        x = 7
        print(f'Local bar: {x}')

    bar()

# print(locals())
print(globals())
# A = 2
print(A)

print(f'Global: {x}')
# foo()
