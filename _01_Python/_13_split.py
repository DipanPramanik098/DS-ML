# Python split() method examples

# 1. Default split (whitespace)
text1 = "Hello world Python"
result1 = text1.split()
print("1. Default split:", result1)  # ['Hello', 'world', 'Python']

# 2. Split by comma
text2 = "apple,banana,cherry"
result2 = text2.split(",")
print("2. Split by comma:", result2)  # ['apple', 'banana', 'cherry']

# 3. Split by dash
text3 = "2025-07-19"
result3 = text3.split("-")
print("3. Split by dash:", result3)  # ['2025', '07', '19']

# 4. Using maxsplit
text4 = "one two three four"
result4 = text4.split(" ", 2)
print("4. Maxsplit = 2:", result4)  # ['one', 'two', 'three four']

# 5. Split by newline
text5 = "line1\nline2\nline3"
result5 = text5.split("\n")
print("5. Split by newline:", result5)  # ['line1', 'line2', 'line3']

# 6. Edge case: empty string
text6 = ""
result6 = text6.split()
print("6. Split empty string:", result6)  # []

# 7. Opposite of split: using join()
list7 = ['apple', 'banana', 'cherry']
result7 = ",".join(list7)
print("7. Using join():", result7)  # 'apple,banana,cherry'
