# Enumerate
for i, char in enumerate('Helllooo'):
    print(i, char)

for i, item in enumerate([1, 2, 3, 4, 5]):
    print(i, item)

for i, item in enumerate((1, 2, 3, 4, 5)):
    print(i, item)

for i, item in enumerate({1, 2, 3, 4, 5}):
    print(i, item)

for i, item in enumerate(list(range(100))):
    if item == 50:
        print(f"Index of 50 is: {i}")
