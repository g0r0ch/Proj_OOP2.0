#
#
#
# print("Я к Вам пишу - чего же боле?")
# print("Что я могу ещё сказать?")
# print("Теперь, я знаю, в вашей воле")
# # print(a)
# # 1/0
# print("Меня презреньем наказать")
# print("Но Вы, к моей несчастной доле")
# print("Хоть каплю жалости храня")
# print("Вы не оставите меня.")

# try:
#     f = open("myfile2.txt")
# except FileNotFoundError:
#     print("impossible to open file")
#
# print("done")

# try:
#     x, y = map(int, input().split())
#     res = x / y
# except (ValueError, ZeroDivisionError):
#     print("Value error")
# # except ZeroDivisionError:
# #     print("ZeroDivisionError")
#
# print("done")

# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ArithmeticError:
#     print("Value error")
# # except ZeroDivisionError:
# #     print("ZeroDivisionError")
#
# print("done")

# try:
#     x, y = map(int, input().split())
#     res = x / y
# except Exception: # common base exception
#     print("Value error")
# # except ZeroDivisionError:
# #     print("ZeroDivisionError")
#
# print("done")

try:
    x, y = map(int, input().split())
    res = x / y
except : # catch all exception
    print("error")
# except ZeroDivisionError:
#     print("ZeroDivisionError")

print("done")