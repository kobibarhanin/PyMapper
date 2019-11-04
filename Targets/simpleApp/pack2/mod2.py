from pack1.mod1 import func1a


def func2a():
    # print(f'{__name__}')
    func1a()


def passer(func):
    func()
