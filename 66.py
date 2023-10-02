# global Keyword
total = 0


def counter():
    global total
    total += 1
    return total


counter()
counter()
print(counter())


total_2 = 0


def count(total_2):
    total_2 += 1
    return total


print(count(count(count(total_2))))
