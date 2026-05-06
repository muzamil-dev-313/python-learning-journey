# Conditional Expression:   # A one-line shortcut for the if-else statement] (tErnary operator)
#                           Print or assign one of two values based on a condition=                          
#                           X if condition else Y

# Positive Number Checker: Write a program that asks the user for a number. If the number is greater than 0, print "The number is positive".
num = int(input("Enter your number: "))

print("The number is positive" if num >= 0 else "The number is negative")

# Even or Odd: Write a program that accepts an integer and checks whether it is even or odd. If the number is divisible by 2, print "Even", otherwise print "Odd".
number = int(input("Enter a number whether the number is even or odd: "))
print("Even" if number % 2 == 0 else "Odd")

x = 9
y = 8
max_num = (x if x > y else y)
min_num = (x if x < y else y)
print(max_num)
print(min_num)

# Voting Eligibility: Take an age as input and if the user is 18 or older, print "You are eligible to vote".
age = int(input("Enter your age: "))

result = ("You are eligible to vote." if age >= 18 else "You are not eligible to vote.")
print(result)

# Equality Check: Create two variables, a and b. If they are equal, print "Both variables are equal".

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

result = ("Both variables are equal." if a == b else 'Both variables are not equal.')
print(result)


# Greater of Two Numbers: Take two numbers as input and print the larger one. If they are equal, print "Both are equal".

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

result = (f'{num1} is larger than {num2}' if num1 > num2 else f'{num2} is larger than {num1}' if num2 > num1 else "Both are equal.")
print(result)


# Password Check: Ask the user to input a password. If the password is "python123", print "Access Granted", otherwise print "Access Denied". 

Password = input("Enter your password: ")

ans = ("Access Granted." if Password == "python123" else "Access Denied.")
print(ans)

# Number Sign Detector: Take a number input and print "Positive", "Negative", or "Zero" based on its value.

Sign_Detector = int(input("Enter your number: "))

result = ("Positive." if Sign_Detector > 0 else "Zero." if Sign_Detector == 0 else "Negative." )
print(result)
