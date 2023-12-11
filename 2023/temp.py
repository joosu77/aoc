class T(tuple):
    def __add__(self, o):
        return T(x+y for x,y in zip(self,o))
    def __add__(self, o):
        return T(x*o for x in self)
    