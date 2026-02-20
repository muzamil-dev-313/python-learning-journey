# Implicit Type Casting
# Python automatically converts one data type to another without user intervention.

x = 10      # int
y = 3.14    # float
z = x + y   # Python converts x to float automatically
print(z)    # 13.14
print(type(z))  # <class 'float'>

# Integer to float
a = 5       # int
b = 2.0     # float
c = a * b   # Result is float: 10.0

# Integer to complex
d = 5       # int
e = 2 + 3j  # complex
f = d + e   # Result is complex: (7+3j)

# Explicit Type Casting
# You manually convert using type conversion functions.

print(int(3.14))      # 3 (truncates decimal)
print(int("123"))     # 123
print(int(True))      # 1
print(int(False))     # 0
# print(int("hello"))  # Error! Can't convert string with letters

# float() - Convert to float
print(float(5))       # 5.0
print(float("3.14"))  # 3.14
print(float("123"))   # 123.0
print(float(True))    # 1.0

# str() - Convert to string
print(str(123))       # "123"
print(str(3.14))      # "3.14"
print(str(True))      # "True"
print(str([1, 2, 3])) # "[1, 2, 3]"

# bool() - Convert to boolean
print(bool(1))        # True
print(bool(0))        # False
print(bool("hello"))  # True
print(bool(""))       # False
print(bool([]))       # False (empty list)
print(bool([1, 2]))   # True
print(bool(None))     # False
