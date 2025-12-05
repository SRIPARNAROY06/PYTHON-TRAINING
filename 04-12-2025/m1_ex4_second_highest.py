def second_highest(nums):
    first = second = None
    for x in nums:
        if first is None or x > first:
            second = first
            first = x
        elif x != first and (second is None or x > second):
            second = x
    return second

if __name__ == "__main__":
    n = int(input("Enter N: "))
    if n < 2:
        print("Need at least 2 numbers.")
    else:
        nums = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
        result = second_highest(nums)
        if result is None:
            print("Second highest does not exist (need two distinct values).")
        else:
            print(f"Second highest value: {result}")

