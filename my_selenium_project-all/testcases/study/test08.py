
def is_subsequence(a, b):
    b = iter(b)
    # print(b)
    #
    # gen = (i for i in a)
    # print(gen)
    #
    # for i in gen:
    #     print(i)
    #
    # gen = ((i in b) for i in a)
    # print(gen)
    #
    # for i in gen:
    #     print(i)

    return all(((i in b) for i in a)) # all只有当所有检查都返回True时，才返回True

print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))

