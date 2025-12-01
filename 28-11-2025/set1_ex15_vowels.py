
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join([ch for ch in text if ch not in vowels])

# Example usage:
print(remove_vowels("Hello World"))  # Output: Hll Wrld
