# Write a program to check whether a person is eligible for voting or not. (accept age from user)
person = int(input("Enter your age: "))

if person >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# #--------------------------------------------------
# Write a program to check whether a number entered by user is even or odd.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd")


# #--------------------------------------------------
# Write a program to check whether a number is divisible by 7 or not.

num1 = int(input("Enter a number: "))

if num1 % 7 == 0:
    print("Number is divisible.")
else:
    print("Number is not divisible")


#--------------------------------------------------
# Write a program to display "Hello" if a number entered by user is a multiple of five ,otherwise print " Bye".

hello = int(input("Enter the number: "))

if hello % 5 == 0:
    print("hello")
else:
    print("bye.")

# #--------------------------------------------------
# Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :

# Unit                              Price
# First 100 units                   no charge
# Next 100 units                    Rs 5 per unit
# After 200 units                   Rs 10 per unit

units = int(input("Enter the unit: "))
bill = 0

if units <= 100:
    bill = 0

if units > 100 and units <=200:
    bill = (units - 100) * 5

if units > 200:
    bill = 500 + (units - 200) * 10

print(bill)


# #--------------------------------------------------
# Write a program to display the last digit of a number. (hint : any number 10 will return the last digit)
# print(456%10)
# print(6%3)
number = int(input("Enter the numnber: "))
digit = number % 10
if digit % 3 == 0:
    print("Last digit of number is divisible by 3")
elif number < 0:
    print("The number is negative.")
else:
    print("Last digit of number is not divisible by 3")

#--------------------------------------------------
# Write a program to accept percentage from the user and display the grade according to the following criteria:
# Marks                           Grade
# > 90                            A
# > 80 and 90                     B
# > 60 and <= 80                  C
# below 60                        D

Marks = int(input("Enter your marks: "))

if Marks > 90:
    print("Grade A")

elif Marks > 80 and Marks <= 90:
    print("Grade B")
elif Marks > 60 and Marks <= 80:
    print("Grade C")
else:
    print("Grade D")

#--------------------------------------------------
# Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
# Cost price (in Rs)                    Tax
# > 100000                              %15
# > 50000 and 100000                    %10
# < = 50000                             %5

cost_prize = int(input("Enter your cost: "))
Tax = 0

if cost_prize > 100000:
    Tax = (15 / 100) * cost_prize

elif cost_prize > 50000 and cost_prize <= 100000:
    Tax = (10 / 100) * cost_prize

else:
    Tax = (5 / 100) * cost_prize

print(f"Tax to be paid {Tax}")


#--------------------------------------------------
# Write a program to check whether an years is leap year or not.
# We fellow the  Gregorian calendar
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



