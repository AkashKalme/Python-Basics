# Scope 2

a = 1


def confusion():
    a = 5
    return a


print(a)
print(confusion())
print(a)


def parent():
    a = 10

    def confusion_2():
        return a
    return confusion_2()


print(a)
print(parent())
print(a)


# 1. Start with local scope
# 2. Parent Local
# 3. GLobal
# 4. Built in Python function
