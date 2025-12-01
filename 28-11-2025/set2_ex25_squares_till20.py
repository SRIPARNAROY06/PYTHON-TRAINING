
def write_squares(filename):
    with open(filename, 'w') as f:
        for i in range(1, 21):
            f.write(f"{i}^2 = {i**2}\n")


write_squares("squares.txt")
