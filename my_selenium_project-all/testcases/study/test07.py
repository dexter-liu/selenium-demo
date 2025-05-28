def get_location(lst, n):
    loc_list =[]
    for loc, target in enumerate(lst):
        if target == n:
            loc_list.append(loc)
    return loc_list

# 使用生成器实现上述代码
def get_location_gen(lst, n):
    for loc, target in enumerate(lst):
        if target == n:
            yield loc


if __name__ == '__main__':
    lst = [1, 2, 2, 4, 5, 2, 7, 8, 9]
    # print(get_location(lst, 8))
    print(list(get_location_gen(lst, 2)))
