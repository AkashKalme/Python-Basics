# Functions

def say_hello():
    print("Hello!")


say_hello()

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


def show_tree():
    fill = '*'
    empty = ' '
    for row in picture:
        for pixel in row:
            if (pixel):
                print(fill, end="")
            else:
                print(empty, end="")
        print()
    print()


show_tree()
show_tree()
show_tree()

print(show_tree)
