# *args and **kwargs
def super_func(*args):
    print(*args)
    print(args)
    return sum(args)


print(super_func(1, 2, 3, 4, 5))


def super_func_2(*args, **kwargs):
    print(*args)
    print(args)
    print(*kwargs)
    print(kwargs)
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + total


print(super_func_2(1, 2, 3, 4, 5, num1=10, num2=5))

# Rule: params, *args, default parameters, **kwargs
