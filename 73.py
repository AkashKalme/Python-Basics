# List Comprehensions
my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# Using list comprehensions
my_list2 = [char for char in 'hello']

print(my_list2)

my_list3 = [num for num in range(0, 100)]

print(my_list3)

my_list4 = [num**2 for num in range(0, 100)]

print(my_list4)

my_list5 = [num**2 for num in range(0, 100) if num % 2 == 0]

print(my_list5)
