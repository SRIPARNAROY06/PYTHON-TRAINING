
def write_lines_to_file(filename):
    lines = [
        "Line 1: Hello",
        "Line 2: Welcome to Python",
        "Line 3: File handling is easy",
        "Line 4: Practice makes perfect",
        "Line 5: End of file"
    ]
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

# Example usage:
write_lines_to_file("sample.txt")
