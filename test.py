# def f(index, lst):
#     return lambda index: lst[index]


def f(index, lst, **kwargs):
    return lst[index]


a = [0, 1, 2, 3, 4, 5]
print(f(1, a, key=lambda x: x > 2))
