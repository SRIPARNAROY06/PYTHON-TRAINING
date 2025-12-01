s=input("Enter a string: ")
is_palindrome=True
for i in range(len(s)):
    if s[i]!=s[len(s)-1-i]:
        is_palindrome=False
        break

if is_palindrome:
    print("The string is palindrome")
else:
    print("The string is not palindrome")