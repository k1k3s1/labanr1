class myclass():
    def __init__(self, x):
        self.x = x
        
    def calc_1(self):
        try:
            if self.x <= 3.087 or self.x >= 1.018:
                return self.x ** 4 * 1.871 + self.x ** 3 * 2.317 - self.x ** 2 * 4.367 + self.x * 3.851
        except TypeError:
            return "Error"

    def calc_2(self):
        try:
            if self.x <= 3.087 or self.x >= 1.018:
                return self.x ** 3 * 5.661 - self.x ** 2 * 3.485 + self.x * 6.331
        except TypeError:
            return "Error"

    def calc_3(self):
        try:
            if self.x <= 3.087 or self.x >= 1.018:
                return self.x ** 2 * 2.642 + self.x * 2.796
        except TypeError:
            return "Error"

    def calc_4(self):
        try:
            if self.x <= 3.087 or self.x >= 1.018:
                return self.x * 5.632
        except TypeError:
            return "Error"

if __name__ == '__main__':
    x = float(input("input float: "))
    m = myclass(x)
    print(m.calc_1())
    print(m.calc_2())
    print(m.calc_3())
    print(m.calc_4())
