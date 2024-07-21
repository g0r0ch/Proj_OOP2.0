#
#
#
class Point:  # = type('Point', (), {'MAX_COORD':100, 'MIN_COORD':0})...type('Point', (B1, B2), {'MAX_COORD':100, 'MIN_COORD':0})
    MAX_COORD = 100
    MIN_COORD = 0


PyDev
console: using
IPython
8.23
.0
Python
3.10
.12(main, Mar
22
2024, 16: 50:05) [GCC 11.4.0]
on
linux
A = type('Point', (), {'MAX_COORD': 100, 'MIN_COORD': 0})
pt = A()


class B1: pass


class B2: pass


A = type('Point', (B1, B2), {'MAX_COORD': 100, 'MIN_COORD': 0})
A.__mro__
Out[7]: (__main__.Point, __main__.B1, __main__.B2, object)


def method1(self):
    print(self.__dict__)
'-----------------------------------------------------------------------------------------------------------'
pt = A()
class B1: pass
class B2: pass
A = type('Point', (B1, B2), {'MAX_COORD': 100, 'method1': method1})
pt = A()
pt.method1()
{}


A = type('Point', (B1, B2), {'MAX_COORD': 100, 'method1': lambda self: self.MAX_COORD})
pt = A()
pt.method1()
Out[15]: 100