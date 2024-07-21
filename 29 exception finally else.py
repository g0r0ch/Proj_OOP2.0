#
#
#
# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError as z:
#     print(z)
#     # print("devision by zero")
# except ValueError as v:
#     print(v)
# # else:
# #     print("nothing wrong happened")
# finally:
#     print("happens anyway")

# try:
#     f = open("myfile.txt")
#     f.write("hello")
# except FileNotFoundError as f:
#     print(f)
# except:
#     print("other err")
#
# finally:
#     if f:
#         f.close()
#         print("file closed")

# try:
#     with open("myfile.txt") as f:
#     f.write("hello")
# except FileNotFoundError as fl:
#     print(fl)
# except:
#     print("other err")

# def get_values():
#     try:
#         x, y = map(int, input().split())
#         return x, y
#     except ValueError as fl:
#         print(fl)
#         return 0, 0
#     finally:
#         print("finally execute before return block")
#
# x, y = get_values()
# print(x, y)

try:
    x, y = map(int, input().split())
    try:
        res = x / y
    except ZeroDivisionError as z:
        print(z)
except ValueError as z:
    print(z)

