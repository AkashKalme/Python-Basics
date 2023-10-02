# Dictionaries: Unordered Key-Value Pair
dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

print(dictionary)
print(dictionary['b'])
# print(dictionary['k'])    # Error

dictionary2 = {
    'a': [1, 2, 3],
    'b': 'hello',
    'c': True
}

print(dictionary2['a'][2])
print(dictionary2['b'][4])

my_list = [
    {
        'a': [1, 2, 3],
        'b': 'hello',
        'c': True
    }, {
        'x': [4, 5, 7],
        'y': 'hii',
        'c': False
    }
]

print(my_list[0]['a'][2])
print(my_list[1]['c'])
