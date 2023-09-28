# Dictionary Keys: Keys must be immutable
dictionary = {
    123: [1, 2, 3],
    123: [4, 5, 6],
    True: 'hello',
    'cde': True,
    # [100]: 45
    '[100]': 56
}

print(dictionary[123])
print(dictionary[True])
print(dictionary['cde'])
# print(dictionary[[100]])
print(dictionary['[100]'])
