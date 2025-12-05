def count_vowels_consonants_digits(string):
    vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    v=c=d=0
    for ch in string:
        if ch.isdigit():
            d+=1
        elif ch.isalpha():
            if ch in vowels:
                v+=1
            else:
                c+=1
    return v,c,d
if __name__ == '__main__':
    string=input('Enter a string: ')
    v,c,d=count_vowels_consonants_digits(string)
    print(f"Vowels: {v}")
    print(f"Consonants: {c}")
    print(f"Digits: {d}")

                