#Given a tuple (10, (20, 30), (40, (50, 60))) , print all integers using recursion.


def print_integers(data):
    for item in data:
        if isinstance(item, int):
            print(item)
        elif isinstance(item, tuple):
            print_integers(item)

nested_tuple = (10, (20, 30), (40, (50, 60)))
print_integers(nested_tuple)

