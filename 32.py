<<<<<<< HEAD
# Dictionary Methods 2
user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print('basket' in user)
print('size' in user)
print('hello' in user.keys())
print('hello' in user.values())
print('hello' in user.items())

print(user.keys())
print(user.values())
print(user.items())

print(user.pop('age'))
print(user.popitem())
print(user)

user.update({'age': 50})
print(user)

user2 = user.copy()
user.clear()
print(user2)
print(user)

user.clear()
print(user)
=======
# Dictionary Methods 2
user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print('basket' in user)
print('size' in user)
print('hello' in user.keys())
print('hello' in user.values())
print('hello' in user.items())

print(user.keys())
print(user.values())
print(user.items())

print(user.pop('age'))
print(user.popitem())
print(user)

user.update({'age': 50})
print(user)

user2 = user.copy()
user.clear()
print(user2)
print(user)

user.clear()
print(user)
>>>>>>> cac0c36b63762f5fc0a069ec23702699f3a86290
