<<<<<<< HEAD
# Set Methods
my_set = {1, 2, 3, 4, 5}
my_set2 = {1, 2, 3}
my_set3 = {4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# .difference()
print(my_set.difference(your_set))

# .discard()
my_set.discard(5)
print(my_set)
my_set.add(5)

# .difference_update()
my_set.difference_update(your_set)
print(my_set)
my_set.add(4)
my_set.add(5)

# .intersection()
print(my_set.intersection(your_set))
print(my_set & your_set)

# .isdisjoint()
print(my_set.isdisjoint(your_set))
print(my_set2.isdisjoint(your_set))

# .union()
print(my_set.union(your_set))
print(my_set | your_set)

# .issubset()
print(my_set.issubset(your_set))
print(my_set3.issubset(your_set))

# .issuperset()
print(my_set.issuperset(your_set))
print(your_set.issuperset(my_set3))
=======
# Set Methods
my_set = {1, 2, 3, 4, 5}
my_set2 = {1, 2, 3}
my_set3 = {4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# .difference()
print(my_set.difference(your_set))

# .discard()
my_set.discard(5)
print(my_set)
my_set.add(5)

# .difference_update()
my_set.difference_update(your_set)
print(my_set)
my_set.add(4)
my_set.add(5)

# .intersection()
print(my_set.intersection(your_set))
print(my_set & your_set)

# .isdisjoint()
print(my_set.isdisjoint(your_set))
print(my_set2.isdisjoint(your_set))

# .union()
print(my_set.union(your_set))
print(my_set | your_set)

# .issubset()
print(my_set.issubset(your_set))
print(my_set3.issubset(your_set))

# .issuperset()
print(my_set.issuperset(your_set))
print(your_set.issuperset(my_set3))
>>>>>>> cac0c36b63762f5fc0a069ec23702699f3a86290
