file_path = "sample.txt"

with open(file_path, "r") as f:
    text = f.read()

lines = text.splitlines()
words = text.split()
chars = len(text)

print(f"Characters: {chars}")
print(f"Words: {len(words)}")
