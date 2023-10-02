# Exercise: Highest Even

def is_even(x):
    return x % 2 == 0


def highest_even(li):
    li.sort()
    li = li[::-1]
    for i in li:
        if (is_even(i)):
            return i


print(highest_even([4, 6, 2, 3, 9, 8]))
