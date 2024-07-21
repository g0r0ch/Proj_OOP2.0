#
#
#
def func2():
    try:
        return 1 / 0
    except:
        print("func error str 8")

def func1():
    try:
        return func2()
    except:
        print("func error str 11")


print("Я к Вам пишу - чего же боле?")
print("Что я могу ещё сказать?")
print("Теперь, я знаю, в вашей воле")
try:
    func1()
except:
    print("func error str 20")
print("Меня презреньем наказать")
print("Но Вы, к моей несчастной доле")
print("Хоть каплю жалости храня")
print("Вы не оставите меня.")
