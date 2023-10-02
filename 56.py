# Default Parameters and Keyword Parameters
def say_hello(name, emoji):
    print(f"Hello {name}{emoji}!")


# Positional Parameters
say_hello("Akash", "😎")
say_hello("😎", "Rahul")

# Keyword Arguments
say_hello(name='Akash', emoji='😎')
say_hello(emoji='😎', name='Rahul')

# Default Parameters


def say_hello_2(name='Darth Vader', emoji='🤖'):
    print(f"Hello {name}{emoji}!")


# Positional Parameters
say_hello_2("Akash", "😎")
say_hello_2("😎", "Rahul")

# Keyword Arguments
say_hello_2(name='Akash', emoji='😎')
say_hello_2(emoji='😎', name='Rahul')

# Default Parameters
say_hello_2()
say_hello_2("Tom")
