# return
def sum(num1, num2):
    return num1 + num2

# Should do one thing really well.
# Should return something.


print(sum(5, 10))

total = sum(10, 5)
print(sum(10, total))


def sum(num1, num2):
    def another_fun(n1, n2):
        return n1 + n2
    return another_fun


total = sum(10, 20)
print(total(10, 20))


def sum(num1, num2):
    def another_fun(n1, n2):
        return n1 + n2
    return another_fun(num1, num2)


total = sum(10, 20)
print(total)
