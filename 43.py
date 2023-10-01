# is vs ==

print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print(10 is 10.0)
print([] == [])
print([1, 2, 3] == [1, 2, 3])

print(1 is 1)
print(1 == 1)

print('1' is 1)
print('1' == 1)

# is checks for location in memory while equality checks for values.
