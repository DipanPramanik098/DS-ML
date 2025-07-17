# python_operators_explained.py

"""
Python Operators - Explained with Examples
==========================================

Operators are special symbols used to perform operations on variables and values.
Python supports the following types of operators:
1. Arithmetic Operators
2. Comparison (Relational) Operators
3. Assignment Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators
"""

print("\n--- 1. Arithmetic Operators ---")
a, b = 10, 3
print("a =", a, "b =", b)
print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)
print("Floor Division (a // b):", a // b)
print("Modulus (a % b):", a % b)
print("Exponentiation (a ** b):", a ** b)

print("\n--- 2. Comparison Operators ---")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\n--- 3. Assignment Operators ---")
x = 5
print("Initial x:", x)
x += 2  # x = x + 2
print("x += 2:", x)
x -= 1
print("x -= 1:", x)
x *= 3
print("x *= 3:", x)
x /= 2
print("x /= 2:", x)
x //= 2
print("x //= 2:", x)
x %= 2
print("x %= 2:", x)
x = 3
x **= 2
print("x **= 2:", x)

print("\n--- 4. Logical Operators ---")
p, q = True, False
print("p =", p, "q =", q)
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

print("\n--- 5. Bitwise Operators ---")
a, b = 5, 3     # In binary: 5 = 0101, 3 = 0011
print("a =", a, "b =", b)
print("a & b (AND):", a & b)     # 0001 = 1
print("a | b (OR):", a | b)      # 0111 = 7
print("a ^ b (XOR):", a ^ b)     # 0110 = 6
print("~a (NOT):", ~a)           # Inverts bits => -(a+1) = -6
print("a << 1 (Left Shift):", a << 1)  # 1010 = 10
print("a >> 1 (Right Shift):", a >> 1) # 0010 = 2

print("\n--- 6. Membership Operators ---")
nums = [1, 2, 3, 4, 5]
print("List:", nums)
print("3 in nums:", 3 in nums)
print("6 not in nums:", 6 not in nums)

print("\n--- 7. Identity Operators ---")
x = [10, 20]
y = [10, 20]
z = x
print("x is z:", x is z)             # True, same object
print("x is y:", x is y)             # False, different objects
print("x == y:", x == y)             # True, same content
print("x is not y:", x is not y)     # True

"""
Summary:
--------

Arithmetic:      +  -  *  /  //  %  **
Comparison:      ==  !=  >  <  >=  <=
Assignment:      =  +=  -=  *=  /=  //=  %=  **=
Logical:         and  or  not
Bitwise:         &  |  ^  ~  <<  >>
Membership:      in  not in
Identity:        is  is not
"""
