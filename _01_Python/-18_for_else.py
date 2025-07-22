# Example 1: Search for an element in a list using for...else
print("Example 1: Searching for 4 in the list")
nums = [1, 3, 5, 7, 9]

for n in nums:
    if n == 4:
        print("Found 4!")
        break
else:
    print("4 not found.\n")  # Runs because no break occurred

# Example 2: for loop with break (so else is skipped)
print("Example 2: Searching for 5 in the list")
nums = [1, 3, 5, 7, 9]

for n in nums:
    if n == 5:
        print("Found 5!")
        break
else:
    print("5 not found.\n")  # Skipped because break occurred

# Example 3: Prime number check using for...else
print("Example 3: Prime number check")
n = 17

for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not prime (divisible by {i})")
        break
else:
    print(f"{n} is prime")  # Runs because no break occurred

