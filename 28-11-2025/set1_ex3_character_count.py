s=input("Enter a string: ")
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
for ch,count in freq.items():
    print(f"{ch}: {count}")