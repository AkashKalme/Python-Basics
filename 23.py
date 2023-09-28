# List Methods
basket = [1, 2, 3, 4, 5]
print(len(basket))

# Append
new_list = basket.append(100)
print(new_list)                     # Append changes the list inplace
print(basket)

new_list = basket
print(new_list)

# Insert
basket.insert(4, 110)
print(basket)

# Extend
basket.extend([6, 7, 8])
print(basket)

# Pop
basket.pop()
print(basket)

basket.pop(0)
print(basket)

# Remove
basket.remove(3)
print(basket)

# Clear
basket.clear()
print(basket)
