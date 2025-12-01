
def second_largest(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    unique_numbers.sort(reverse=True)    # Sort in descending order
    return unique_numbers[1] if len(unique_numbers) > 1 else None

# Example usage:
nums = (10, 20, 4, 45, 99)
result = second_largest(nums)
print(result)  # Output: 45
