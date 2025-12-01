
def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

# Example usage:
print(primes_in_range(10, 30))  # Output: [11, 13, 17, 19, 23, 29]
