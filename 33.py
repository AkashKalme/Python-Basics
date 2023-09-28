# Tuple: Immutable Lists
my_tuple = (1, 2, 3, 4, 5)

# my_tuple[1] = 3       # Error

print(my_tuple)
print(my_tuple[1])
print(my_tuple[3:])

print(4 in my_tuple)
print(6 in my_tuple)

user = {
    (1, 2): [1, 2, 3],
    'greet': 'hello',
    'c': True
}

print(user)
print(user.items())
print(user[(1, 2)])
