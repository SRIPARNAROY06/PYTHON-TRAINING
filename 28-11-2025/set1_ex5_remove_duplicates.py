numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Original list:", numbers)

num_list = []
for number in numbers:
    if number not in num_list:
        num_list.append(number)

print("List without duplicates:", num_list)
