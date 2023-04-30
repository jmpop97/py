class test:
    def __init__(self):
        self.hp = 100

    def ms(self):
        self.hp -= 1


a = 0
b = test()
try:
    while a < 100:
        a += 1
        b.ms()
        if a == 10:
            raise
except:
    pass
c = [a, b.hp]
print(c)


def test2(a, b):
    try:
        while a < 100:
            a += 1
            b.ms()
            if a == 10:
                raise
    except:
        pass


a = 0
b = test()
test2(a, b)
c = [a, b.hp]
print(c)
