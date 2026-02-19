# Variable naming rules:
# - Can contain letters, numbers, underscores
# - Cannot start with a number
# - Case-sensitive (Age and age are different)
# - Cannot use reserved keywords (if, else, while, etc.)

name = "Muzamil."    # string
age = 21            # integer
height = 5.5        # float
is_student = True   # boolean

print("My name is",name, "I'm", age, "years old.", "My height is", height, "and I'm a student. Its" ,is_student )

a = "Muzamil"
b = 7
c = 7.7
d = False
f = complex(9, + 5)

print(a , b)
print(a)
print(b)

print(type(a))
print(type(b))

print(d)
print("The type of d is", type(d))

print(f)

# Integer (int)
age = 21
negative = -10
big_number = 1_000_000  # Underscores for readability

# Float (float)
price = 59.99
pi = 3.14159
scientific = 1.5e-3  # 0.0015
print(scientific)

# Complex (complex)
complex_num = 3 + 4j

is_valid = True
is_finished = False

# Boolean from comparisons
result = 10 > 5  # True
print(result)

# Different ways to create strings
name = 'Python'
message = "Hello World"
multiline = """This is
a multiline
string"""

# String operations
first = "Hello"
last = "World"
full = first +" " + last  # Concatenation: "Hello World"
repeat = "Ha" * 3          # "HaHaHa"
print(full)
print(repeat)

# String indexing and slicing
text = "Python"
print(text[0])    # 'P' (first character)
print(text[-1])   # 'n' (last character)
print(text[1:4])  # 'yth' (characters from index 1 to 3)
print(text[:3])   # 'Pyt' (first 3 characters)

# String methods
text.upper()      # Convert to uppercase
text.lower()      # Convert to lowercase
text.strip()      # Remove whitespace
text.split()      # Split into list
print(text.upper())

# Collection Data Types
# List (list) - Mutable, ordered
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4]]

# List operations
fruits.append("grape")     # Add item
fruits.remove("banana")    # Remove item
fruits[0] = "pear"         # Modify item
print(fruits[1])           # Access item

# Tuple (tuple) - Immutable, ordered
coordinates = (10, 20)
rgb = (255, 128, 0)
single_item = (1,)  # Comma needed for single item

# Accessing tuple items
x = coordinates[0]
y = coordinates[1]

# Tuple unpacking
x, y = coordinates

# Dictionary (dict) - Key-value pairs -------------


# Set (set) - Unordered, unique items -------------
