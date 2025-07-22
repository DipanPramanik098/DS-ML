# range(stop)
print("Example 1: range(5) — prints numbers from 0 to 4")
for i in range(5):
    print(i, end=' ')
print("\n")  # New line

# range(start, stop)
print("Example 2: range(2, 6) — prints numbers from 2 to 5")
for i in range(2, 6):
    print(i, end=' ')
print("\n")

# range(start, stop, step)
print("Example 3: range(1, 10, 2) — prints odd numbers from 1 to 9")
for i in range(1, 10, 2):
    print(i, end=' ')
print("\n")

# Reverse counting
print("Example 4: range(10, 0, -1) — reverse from 10 to 1")
for i in range(10, 0, -1):
    print(i, end=' ')
print("\n")

# Converting range to list
print("Example 5: Convert range to list")
print("list(range(5)) =", list(range(5)))
print("list(range(2, 10, 2)) =", list(range(2, 10, 2)))
print()

# Looping with range and indexing
print("Example 6: Looping through a list using range(len(list))")
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"Index {i} -> {fruits[i]}")
