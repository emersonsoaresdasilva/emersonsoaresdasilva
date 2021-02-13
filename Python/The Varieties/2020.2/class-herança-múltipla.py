class A:
    def __init__(self, x):
        self.x = x

    def get_x(self):
        return self.x

class B:
    def __init__(self, y):
        self.y = y

    def get_y(self):
        return self.y

class C(A, B):
    def __init__(self, x, y):
        A.__init__(self, x)
        B.__init__(self, y)

# Programa principal:
obj = C(2, 5)
print(obj.x)
print(obj.y)
print(obj.get_x())
print(obj.get_y())
