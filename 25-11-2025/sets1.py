nums={10,20,30,40,50}
#sets dont allow duplicates
data={1,2,2,3,3,3}
print(data) #1,2,3

#creating a set
s2={10,20,30}
empty=set()

#add operations
s={1,2,3}
s.add(4)
print(s)
s.update([5,6])

#remove operations
s.remove(3)#throws an error if not present
s.discard(10)#does nothing if not found
s.pop()#removes a random element
print(s)
print(s)