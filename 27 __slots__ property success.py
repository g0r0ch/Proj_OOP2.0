#
#
#

class Point2D:
    # __slots__ = ('x', 'y', '__length') # object has no attribute '__dict__'   slots collection prohibit only local class instance
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.length = (x * x + y * y) ** 0.5

class Point3D(Point2D): # contains __dict__ collect if __slots__ miss
    __slots__ = 'z',  # cause tuple
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z



    # @property
    # def length(self): # non local veriable class instance but attribute Point2D clas
    #     return self.__length
    #
    # @length.setter
    # def length(self, value):
    #     self.__length = value