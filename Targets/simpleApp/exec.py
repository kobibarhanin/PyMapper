import sys

from pack1.mod1 import func1a
from pack2.mod2 import func2a, passer
from Mapper.mapper import trace_calls

def passable():
    print(f'{__name__}')


def run():
    print(f'{__name__}')
    func1a()
    func2a()
    passer(passable)


if __name__ == '__main__':
    import os
    os.remove('stack_log.txt')
    sys.settrace(trace_calls)
    run()
