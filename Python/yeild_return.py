def a(temp):
    haha = yield temp+1
    return haha


def func():
    for i in range(10):
        yield i


temp = a
b = temp.send(None)
c = temp.send(2)
pass
