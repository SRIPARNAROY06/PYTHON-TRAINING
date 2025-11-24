#Printing
name="Sriparna"
age= 22
salary=4.5

print(name)
print(age)
print(salary)

#Operators
a=10
b=3

print("Addition: ", a + b)
print("Division: ", a / b)
print("Floor Division: ", a // b)
print("Modulus: ", a % b)
print("power: ", a ** b)

#Conditional Statements
marks=int(input("Enter your score:"))

if marks >=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks >=60:
    print("Grade C")
else:
    print("Grade D")
    
#loop 
for i in range(1,6):
    print("Number: ")


#list of number till 20 where 1 is odd and 2 is even
for i in range(1,21):
    if i%2 ==0:
        print(i, "is even")
    else:
        print(i ,"is odd")

#for loop
for i in range(1,6):
    print("Number: ",i)


#while    
counter=1    
while counter <=5:
    print("Count", counter)
    counter+=1
    #counter=counter +1


#break
for i in range (10):
    if i == 5:
        break
    print(i)

#continue
for i in range (10):
    if i % 2==0:
        continue
    print(i)
    
