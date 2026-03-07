# Incrementing while loop
i = 1
while i < 10:
    print(i)
    i += 1
print(i)

while i < 55:
    i = int(input("Enter your favorite number: "))
    print(i)

# decrementing while loop

num = int(input("Enter the number: "))

while num >= 0:
    print(num)
    num -= 1

count = 5
while count > 0:
    print(count)
    count = count - 1
else:
    print("I am inside else")


while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number >= 0:
    break

