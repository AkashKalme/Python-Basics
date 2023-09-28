# List Slicing
import copy

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

print(amazon_cart)
print(amazon_cart[0::2])

amazon_cart[0] = 'laptop'
print(amazon_cart)
print(amazon_cart[0:3])

new_cart = amazon_cart[0:4]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

new_cart2 = amazon_cart
new_cart2[0] = 'books'
print(new_cart2)
print(amazon_cart)

copy_cart = copy.copy(amazon_cart)
copy_cart[0] = 'pencils'
print(copy_cart)
print(amazon_cart)

copy_cart2 = copy.deepcopy(amazon_cart)
copy_cart2[0] = 'mobiles'
print(copy_cart2)
print(amazon_cart)
