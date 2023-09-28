# List Methods 2
basket = ['a', 'b', 'c', 'd', 'e', 'b']

# Index
print(basket.index('b'))
# print(basket.index('f'))           # Error
# print(basket.index('d', 0, 3))     # Error
print(basket.index('d', 0, 4))

# in
print('d' in basket)
print('x' in basket)

# Count
print(basket.count('b'))
print(basket.count('f'))
