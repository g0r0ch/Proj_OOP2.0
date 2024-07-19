# private __ - свойства или методы закрытые от внешнего вмешательства, доступные только внутри класса НЕ доступные в т.ч. из дочерних
# protected _ - атрибут доступный в классе и во всех дочерних НЕ
# class Geom:
#     name = 'Geom'
# # if '__' added then '_Geom__x1': 0 else 'x1': 0 when print
#     def __init__(self, x1, y1, x2, y2):
#         print(f"Geom initialise for {self.__class__}")
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2

class Geom:
    __name = 'Geom'
# if '__' added then '_Geom__x1': 0 else 'x1': 0 when print
    def __init__(self, x1, y1, x2, y2):
        print(f"Geom initialise for {self.__class__}")
        self.__verify_coord(x1) # только в классе, где определён метод else protected #
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._name = self.__name

    def get_coords(self):
        return (self.__x1, self.__y1)

    # только в классе, где определён метод
    def __verify_coord(self,coord):
        return 0 <= coord < 100

class Rect(Geom):

    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self.__fill = fill
        # self.__name = Geom.__name
# AttributeError:
    # def get_coords(self):
    #     return (self.__x1, self.__y1)
    def get_coords(self):
        return (self._x1, self._y1)

r = Rect(0, 0, 10, 20)
r.get_coords()
print(r.__dict__)