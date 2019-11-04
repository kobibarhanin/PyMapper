import sys

from pack1.mod1 import func1a
from pack2.mod2 import func2a, passer

from Mapper import Mapper

def passable():
    # print(f'{__name__}')
    pass


def run():
    # print(f'{__name__}')
    func1a()
    func2a()
    passer(passable)


if __name__ == '__main__':

    sys.settrace(Mapper('mapping_rules').trace_calls)
    run()

