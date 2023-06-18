class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, a, b):
        return self.a + self.b

    def sub(self, a, b, reverse=False):
        if reverse:
            return self.b - self.a
        else:
            return self.a - self.b

    def mul(self, a, b):
        return self.a * self.b

    def div(self, a, b, reverse=False):
        if reverse:
            return self.b / self.a
        else:
            return self.a / self.b