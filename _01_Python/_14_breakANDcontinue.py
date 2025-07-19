# Python break and continue examples

# 1. Using break in a loop
print("1. Using break:")
for i in range(1, 10):
    if i == 5:
        print("  Break at", i)
        break  # exits the loop completely
    print("  i =", i)

print("\n2. Using continue:")
# 2. Using continue in a loop
for i in range(1, 6):
    if i == 3:
        print("  Skip", i)
        continue  # skips the rest of the loop body for this iteration
    print("  i =", i)

print("\n3. break with while loop:")
# 3. break in a while loop
x = 0
while x < 10:
    if x == 4:
        print("  Breaking at", x)
        break
    print("  x =", x)
    x += 1

print("\n4. continue with while loop:")
# 4. continue in a while loop
x = 0
while x < 5:
    x += 1
    if x == 3:
        print("  Skipping", x)
        continue
    print("  x =", x)
