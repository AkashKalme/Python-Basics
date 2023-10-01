# Iterable - List, Set, Tuple, String, Dictionary
user = {
    "name": "Gotham",
    "age": 5006,
    "can_swim": False
}

# Normal
for item in user:
    print(item)

# Items
for item in user.items():
    print(item)

# Keys
for item in user.keys():
    print(item)

# Values
for item in user.values():
    print(item)

# Key-Value
for key, value in user.items():
    print(key, value)
