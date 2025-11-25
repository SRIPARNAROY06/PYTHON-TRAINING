nums=[10,11,12,13,17,20,23]
prime_nos=[]
for i in  nums:
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c==1:
        prime_nos.append(i)

print(prime_nos)