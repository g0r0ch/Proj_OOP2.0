#
#
#

class Women:
    title = 'class obj field title'
    photo = 'class obj field photo'
    ordering = 'class obj field ordering'

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + '@' + psw)

    class Meta:                              # iternal class shouldn't use external class
        ordering = ['id']

        def __init__(self, access):
            self.access = access

w = Women('root', '12345')
print(Women.ordering)
print(Women.Meta.ordering) # attached class call
print(w.__dict__)
print(w.meta.__dict__)