# Formatted Strings
name = "Akash"
age = 23
print("Hi, " + name + ". You are " + str(age) + " years old.")
print(f"Hi, {name}. You are {age} years old.")
print("Hi, {}. You are {} years old.".format("Akash", "23"))
print("Hi, {}. You are {} years old.".format(name, age))
print("Hi, {1}. You are {0} years old.".format(age, name))
print("Hi, {new_name}. You are {new_age} years old.".format(
    new_name="Akash", new_age="23"))
