
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Example usage:
print(longest_word("Write a function that finds the longest word"))

