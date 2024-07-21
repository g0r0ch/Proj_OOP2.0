#MRO - Method Resolution Order
#for mixins usage
#MRO only one Param(self)
class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")

class MixinLog:
    ID = 0

    #def __init__(self, p1):
    def __init__(self):
        super().__init__()
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID

# class MixinLog2:
#         # def __init__(self):
#     def __init__(self):
#         super().__init__()
#         print("init MixinLog2")

    def save_sell_log(self):
        print(f"{self.id}: staff was saled in 00:00 h")

    def print_info(self):
        print("print_info from MixinLog")

class NoteBook(Goods, MixinLog):
    #
    def print_info(self):
        MixinLog.print_info(self) # if method in both classe ancess and success!!


n = NoteBook("Acer", 1.5, 30000)
MixinLog.print_info(n)
# n.print_info()
# n.save_sell_log()
# print(NoteBook.__mro__)