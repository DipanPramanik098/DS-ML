# Python List Examples

print("1. Creating a list:")
fruits = ["apple", "banana", "cherry"]
print("  fruits =", fruits)

print("\n2. Accessing elements:")
print("  First fruit:", fruits[0])
print("  Last fruit:", fruits[-1])

print("\n3. Modifying elements:")
fruits[1] = "blueberry"
print("  Updated fruits:", fruits)

print("\n4. Adding elements:")
fruits.append("orange")  # Add to end
fruits.insert(1, "mango")  # Insert at index 1
print("  After adding:", fruits)

print("\n5. Removing elements:")
fruits.remove("apple")  # Remove by value
last = fruits.pop()     # Remove last
print("  After removing:", fruits)
print("  Popped element:", last)

print("\n6. List length and membership:")
print("  Length of list:", len(fruits))
print("  Is 'cherry' in list?", "cherry" in fruits)

print("\n7. Iterating through list:")
for fruit in fruits:
    print("  -", fruit)

print("\n8. List slicing:")
print("  First two:", fruits[:2])
print("  Last two:", fruits[-2:])

print("\n9. Sorting and reversing:")
nums = [3, 1, 4, 2]
nums.sort()
print("  Sorted nums:", nums)
nums.reverse()
print("  Reversed nums:", nums)

print("\n10. Nested lists:")
matrix = [[1, 2], [3, 4]]
print("  matrix[1][0] =", matrix[1][0])  # Accessing nested element
