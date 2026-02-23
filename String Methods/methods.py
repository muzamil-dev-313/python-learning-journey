name = "muZaMil1"
A = "Hello World!!!!"
StudentOf = "Balochistan University Of Information Technology, Engineering  & Management Sciences"

print(len(name))
print(name.lower())
print(name.capitalize())
print(name.replace("muZaMil", "Ali Reza"))
print(name.isalnum()) # It's an Alpha numeric Sting the output is True.      A-Z,   a-z, or 0-9. If any other characters or punctuatins are present, then it returns False.\
print(name.isalpha()) # True only if entire string only consists of A-Z, a-z.
print(name.islower())
print(name.istitle())

print(A.find("W"))
print(A.rstrip("!"))
print(A.endswith("d"))
# print(A.join("Ali"))
print(A.isprintable()) #True if all the values within the given string are printable, if not, then return False.


print(StudentOf.split())
print(StudentOf.upper())
print(StudentOf.count("i"))
print(StudentOf.endswith("s"))
print(StudentOf.center(100))
print(StudentOf.isspace())  # Only space comes the True otherwise false
print(StudentOf.istitle())



string = "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics."

print(string.startswith("Python"))
print(string.swapcase())
print(string.title())
print(string.format())
print(string.index("w"))
print(string.format_map(string))
print(string.isdecimal())
