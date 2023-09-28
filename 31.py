# Dictionary Methods
user = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}

user2 = {
    'basket': [4, 7, 8],
    'greet': 'hi',
    'age': 20
}

# print(user['age'])            # Error
print(user.get('age'))
print(user.get('age', 50))

print(user2.get('age', 50))

user3 = dict(name='Akash')
print(user3)
