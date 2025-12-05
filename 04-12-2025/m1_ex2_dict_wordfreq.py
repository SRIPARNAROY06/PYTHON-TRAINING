
def wrd_freq(text):
    text = text.lower()
    words = text.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

if __name__ == "__main__":
    text = input("Enter a string: ")
    freq = wrd_freq(text)

    # Print each word and its frequency
    print("Word frequencies:")
    for word, count in freq.items():
        print(f"{word}: {count}")
        
