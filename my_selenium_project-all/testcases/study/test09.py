b = (i for i in range(5))
print(b)
print(2 in b)
print(4 in b)
print(3 in b)


a = iter(i for i in range(5))
print(list(a))
print(list(a))

