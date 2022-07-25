# def foo():
#     print('FOO')
#     print('FOO')
#     print('FOO')
#
# foo()
# foo()

print(globals())
print(locals())

class Foo:
    print('FOO')
    print('FOO')
    print('FOO')
    y = example()

    def foo(self):
        example()


def example():
    print('EXAMPLE')
# f1 = Foo()
# f1.f()