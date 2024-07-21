#
# print("Я к Вам пишу - чего же боле?")
# print("Что я могу ещё сказать?")
# print("Теперь, я знаю, в вашей воле")
# e = ZeroDivisionError("Division by zero")
# raise e
# print("Меня презреньем наказать")
# print("Но Вы, к моей несчастной доле")
# print("Хоть каплю жалости храня")
# print("Вы не оставите меня.")

class ExceptionPrint(Exception):
    """Common Exception class data send to print"""


class ExceptionPrintSendData(ExceptionPrint):
    """Exception class data send to print"""
    def __init__(self, *args):
        self.message = args[0] if args else None
    def __str__(self):
        return f"Error: {self.message}"
class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"print: {str(data)}")

    def send_data(self, data):
         if not self.send_to_print(data):
             # raise Exception("no answer")
             raise ExceptionPrintSendData("no answer")

    def send_to_print(self, data):
        return False


p = PrintData()

try:
    p.print("123")
except ExceptionPrintSendData:
    print("no answer 2")
except ExceptionPrint:
    print("Common print error")











