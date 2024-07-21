#
##

class Geom:                 # if somewhere get_pr miss
    def get_pr(self):
        #return -1
        raise NotImplementedError("successor class missed method  get_pr()")

class Rectangle(Geom):

    def __init__(self, w, h):
        self.w = w
        self.h = h

    # def get_rect_pr(self):
    def get_pr(self):
        return 2*(self.w+self.h)


class Square(Geom):

    def __init__(self, a):
        self.a = a

    #def get_sq_pr(self):
    def get_pr(self):
        return 4 * self.a

class Triangle(Geom):

        def __init__(self, a, b , c):
            self.a = a
            self.b = b
            self.c = c

        #def get_tr_pr(self):
        def get_pr(self):
            return self.a + self.b + self.c



geom = [Rectangle(1 , 2), Rectangle(3 , 4),
        Square(10), Square(20),
        Triangle(1, 2, 3), Triangle(4, 5, 6)]

# r1 = Rectangle(1 , 2)
# r2 = Rectangle(3 , 4)
# s1 = Square(10)
# s2 = Square(20)
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
#
# geom = [r1, r2, s1, s2, t1, t2]
for g in geom:
    print(g.get_pr())
    # if isinstance(g, Rectangle):
    #     print(g.get_rect_pr())
    # else:
    #     print(g.get_sq_pr())
# print(r1.get_rect_pr(), r2.get_rect_pr())
# print(s1.get_sq_pr(), s2.get_sq_pr())