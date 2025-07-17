# slice_explained.py

"""
Python Slice Explained in Detail
================================

In Python, slicing is a powerful feature that allows extracting parts of sequences like:
- strings
- lists
- tuples

Slicing uses the following syntax:
    sequence[start:stop:step]

Where:
- start: the index to begin the slice (inclusive)
- stop: the index to end the slice (exclusive)
- step: the step/increment between elements

Note:
- Negative indices count from the end (-1 is the last element)
- Default start = 0, stop = len(sequence), step = 1 if omitted

Python also has a `slice()` built-in object that does the same thing.
"""

# === Slicing a List ===
nums = [10, 20, 30, 40, 50, 60, 70, 80]

# Basic slicing
print("Original List:", nums)
print("nums[1:5] =>", nums[1:5])       # [20, 30, 40, 50]
print("nums[:4] =>", nums[:4])         # [10, 20, 30, 40]
print("nums[3:] =>", nums[3:])         # [40, 50, 60, 70, 80]
print("nums[:] =>", nums[:])           # full copy: [10, 20, 30, 40, 50, 60, 70, 80]

# With step
print("nums[::2] =>", nums[::2])       # [10, 30, 50, 70]
print("nums[1:7:2] =>", nums[1:7:2])   # [20, 40, 60]

# Negative indexing
print("nums[-3:] =>", nums[-3:])       # [60, 70, 80]
print("nums[:-2] =>", nums[:-2])       # [10, 20, 30, 40, 50, 60]
print("nums[::-1] =>", nums[::-1])     # reversed list: [80, 70, ..., 10]

# === Slicing a String ===
text = "PythonSlice"

print("\nOriginal String:", text)
print("text[0:6] =>", text[0:6])       # 'Python'
print("text[6:] =>", text[6:])         # 'Slice'
print("text[::-1] =>", text[::-1])     # 'ecilSnohtyP'

# === Using the slice() object ===
s = slice(1, 5)     # same as [1:5]
print("\nUsing slice() object:")
print("slice(1, 5) applied to nums =>", nums[s])  # [20, 30, 40, 50]

# slice with step
s2 = slice(0, 8, 2)
print("slice(0, 8, 2) applied to nums =>", nums[s2])  # [10, 30, 50, 70]

# dynamic slicing
start = 2
end = 6
step = 2
s3 = slice(start, end, step)
print(f"slice({start}, {end}, {step}) =>", nums[s3])  # [30, 50]

# === Slicing a Tuple ===
tup = (1, 2, 3, 4, 5, 6)
print("\nSlicing a tuple:")
print("tup[1:4] =>", tup[1:4])         # (2, 3, 4)

# === Advanced Tips ===

# 1. Slice assignment (lists only, not strings or tuples)
nums[0:3] = [100, 200, 300]
print("\nAfter slice assignment nums[0:3] = [100, 200, 300] =>", nums)

# 2. Deleting slice
del nums[3:5]
print("After deleting nums[3:5] =>", nums)

"""
Conclusion:
-----------
Slicing is an elegant and fast way to extract or manipulate parts of a sequence in Python.

You can:
- Read a slice
- Assign to a slice (for mutable types like lists)
- Delete a slice
- Use slice objects for reusability

It's widely used in data processing, algorithms, string manipulation, and more.
"""
