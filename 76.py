# Exercise: Comprehensions
some_list = ['a', 'b', 'c', 'b', 'm', 'n', 'n']

duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))

print(duplicates)
