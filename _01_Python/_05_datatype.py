import sys

# This script demonstrates various Python data types and their sizes.


a = 2;
b = 12.22;
c = "Hello World";
d = True;
e = None;
f = [1, 2, 3, 4, 5];
g = (1, 2, 3, 4, 5);
h = {1, 2, 3, 4, 5};
i = {"name": "Alice", "age": 30, "city": "New York"};
j = range(5);
k = bytearray(5);
l = bytes(5);
m = memoryview(bytes(5));
n = complex(1, 2);


print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>   
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>
print(type(e))  # <class 'NoneType'>
print(type(f))  # <class 'list'>
print(type(g))  # <class 'tuple'>
print(type(h))  # <class 'set'>
print(type(i))  # <class 'dict'>
print(type(j))  # <class 'range'>
print(type(k))  # <class 'bytearray'>
print(type(l))  # <class 'bytes'>
print(type(m))  # <class 'memoryview'>
print(type(n))  # <class 'complex'>

print(sys.getsizeof(a))  # Size of int
print(sys.getsizeof(b))  # Size of float