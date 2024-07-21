#
#
#
# fp = None
# try:
#     fp = open("file.txt")
#     for t in fp:
#         print(t)
# except Exception as e:
#     print(e)
# finally:
#     if fp is not None:
#         fp.close(

# fp = None
# try:
#     with open("file.txt") as  f# with close file __enter__ as start __exit__ as finish
#     for t in fp:
#         print(t)
# except Exception as e:
#     print(e)

class DefendVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp

        return False


v1 = [1, 2 , 3]
v2 = [2, 3]

try:
    with DefendVector(v1) as dv:
        for i, a in enumerate(dv):
            dv[i] += v2[i]
except:
    print("Error")
print(v1)