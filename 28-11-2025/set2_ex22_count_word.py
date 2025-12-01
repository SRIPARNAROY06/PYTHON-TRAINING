
def count_python_lines(filename):
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            if "Python" in line:
                count += 1
    return count

# Example usage:
print(count_python_lines("sample.txt"))
