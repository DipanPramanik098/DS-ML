# Python pass statement examples

print("1. Using pass in an empty if block:")
x = 10
if x > 5:
    pass  # Placeholder: do nothing for now
print("  Code continues after pass")

print("\n2. Using pass inside a loop:")
for i in range(5):
    if i == 2:
        pass  # Do nothing when i == 2
    print("  i =", i)

print("\n3. Using pass to define an empty function:")
def future_function():
    pass  # Function logic will be added later

future_function()
print("  Called an empty function using pass.")

print("\n4. Using pass in an empty class:")
class MyClass:
    pass  # Empty class definition

obj = MyClass()
print("  Created an object of an empty class.")
