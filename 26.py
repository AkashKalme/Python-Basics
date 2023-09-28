# Common List Patterns
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'b']

# Sort
basket.sort()

# Reverse
basket.reverse()
print(basket[::-1])

# Length of List
print(len(basket))

# Range
print(range(1, 100))
print(list(range(1, 100)))
print(list(range(101)))

# Join
sentence = '!'
new_sentence = sentence.join(['Hi', 'my', 'name', 'is', 'Akash!'])
print(new_sentence)

new_sentence2 = ' '.join(['Hi', 'my', 'name', 'is', 'Akash!'])
print(new_sentence2)
