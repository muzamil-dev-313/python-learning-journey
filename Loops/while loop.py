user = ""
while user != "Hello":
    user = input("Enter your password: ")
print("Welcome our website.")

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

# Questionsl


#-----------------------------------------------------------------------------
# Print numbers from 1 to 10 using a while loop.
num = 1
while num <= 10:
    print(num)
    num += 1

#-----------------------------------------------------------------------------
# Print numbers from 10 to 1 (reverse order).
num = 10
while num > 0:
    print(num)
    num -= 1

#-----------------------------------------------------------------------------
# Print even numbers from 1 to 20 using a while loop.
num = 1
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1

#-----------------------------------------------------------------------------
# Print odd numbers from 1 to 15.
num = 0
while num <= 15:
    if num % 2:
        print(num)
    num += 1

#-----------------------------------------------------------------------------
# Print the first 10 multiples of 5.
num = 5
count = 1

while count <= 10:
    print(num)
    num += 5
    count += 1

# OR 

num = 1
while num <= 10:
    print(num * 5)
    num += 1
#-----------------------------------------------------------------------------
while True:
    num = int(input("Enter a number: "))
    if num == 10:
        print(5 * num)
        num += 1
        break
    else:
        print("Invalid number try again.")
