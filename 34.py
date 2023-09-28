# Tuples 2
my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple[1:2]

print(new_tuple)

new_tuple2 = my_tuple[1:4]
print(new_tuple2)

a, b, *other, d = (1, 2, 3, 4, 5, 6, 7, 8)
print(a)
print(b)
print(other)
print(d)

my_tuple2 = (1, 2, 3, 4, 5, 6, 7, 5, 5, 5)

print(my_tuple2.count(5))
print(my_tuple2.count(3))
print(my_tuple2.index(5))
print(my_tuple2.index(3))
print(len(my_tuple2))
