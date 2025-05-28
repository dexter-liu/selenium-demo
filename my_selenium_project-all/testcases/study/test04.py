from typing import Iterable


def is_iterable(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False

params = [
    1234,
    '1234',
    [1, 2, 3, 4],
    {1, 2, 3, 4},
    {1: 1, 2: 2, 3: 3, 4: 4},
    (1, 2, 3, 4)
]

params2 = [
    1234,
    '1234',
    [1, 2, 3, 4],
    {1, 2, 3, 4},
    {1: 1, 2: 2, 3: 3, 4: 4},
    (1, 2, 3, 4)
]

for param in params:
    print('{} is iterable? {}'.format(param, is_iterable(param)))

print('-----------------------')
for param in params2:
    print('{} is iterable? {}'.format(param, isinstance(param, Iterable)))