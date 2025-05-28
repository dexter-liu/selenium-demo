# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# l3 = l2
#
# print(id(l1))
# print(id(l2))
# print(id(l3))
#
# print(l1 is l2)
# print(l2 is l3)


def func(d):
    d['a'] = 10
    d['b'] = 20

d = {'a': 1, 'b': 2}
func(d)
print(d)