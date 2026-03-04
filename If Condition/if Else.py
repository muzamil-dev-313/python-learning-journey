# Question No. 01

# Write a program that calculates the price of a movie ticket based on the person's age and whether they want a 3D movie or not.

# Requirements:

# Ask the user to enter their age

# Ask the user if they want a 3D movie (yes or no)

# Calculate the ticket price based on these rules:

# Children (age 0-12): $8 for regular, $12 for 3D

# Adults (age 13-64): $12 for regular, $18 for 3D

# Seniors (age 65+): $10 for regular, $15 for 3D

# If someone enters a negative age, show an error message

# Display the final ticket price

age = int(input("Enter your age: "))

movie = input("Do you want a 3D movie? (yes or no ?)")

if age < 0:
    print("Invalid age! Please enter a valid age.")

elif (age <= 12):
    if (movie == "yes"):
        price = 12
    else:
        price = 8
    print(f"Your ticket price is: ${price}")
elif (age >=13 and age <= 64):
    if(movie == "yes"):
        price = 18
    else:
        price = 12
    print(f"Your ticket price is: ${price}")
elif (age >= 65):
    if (movie == "yes"):
        price = 15
    else:
        price =10
    print(f"Your ticket price is: ${price}")


#------------------------------------------------------------------------------------------------------

# Question No. 02
# Temperature Alert System (Using only if-elif-else)

# Write a program that gives safety advice based on temperature input.

# Requirements:

# Ask the user to enter the temperature in Celsius

# Provide appropriate advice based on these ranges:

# Below 0°C: "Freezing cold! Wear heavy winter clothes"

# 0°C to 15°C: "Cold weather! Wear a jacket"

# 16°C to 25°C: "Pleasant weather! Enjoy your day"

# 26°C to 35°C: "Warm weather! Stay hydrated"

# Above 35°C: "Very hot! Stay indoors and drink plenty of water"

# If temperature is exactly 0°C, include it in the "Cold weather" category

Celsius = int(input("Enter the temperature in Celsius: "))

if Celsius < 0:
    print("Freezing cold! Wear heavy winter clothes")
elif Celsius == 0:
    print("Cold weather")
elif Celsius <= 15:
    print("Cold weather! Wear a jacket")
elif Celsius <= 25:
    print("Pleasant weather! Enjoy your day")
elif Celsius <= 35:
    print("Warm weather! Stay hydrated")
else:
    print("Very hot! Stay indoors and drink plenty of water")


#------------------------------------------------------------------------------------------------------

# Question No. 03
# Library Fine Calculator (Using if-elif-else with nested if)
# A library charges fines for late book returns. Write a program to calculate the fine.

# Requirements:

# Ask the user for:

# Number of days late

# Type of book (regular, children's, or reference)

# Fine calculation rules:

# Regular books:

# First 5 days: $1 per day

# 6-10 days: $2 per day

# More than 10 days: $5 per day + $10 extra penalty

# Children's books:

# First 7 days: $0.50 per day

# 8-15 days: $1 per day

# More than 15 days: $2 per day + $5 extra penalty

# Reference books:

# Cannot be late! $10 per day + $20 penalty

# If days late is negative, show error message

# Display the total fine amount

number_of_days_late = int(input("Enter days late: "))
book_type = input("Enter book type (regular/childrens/reference): ")

if number_of_days_late < 0:
    print("Invalid days! Please enter valid number of days.")
else:

    if book_type == "regular":
        if number_of_days_late <= 5:
            fine = number_of_days_late * 1
        
        elif number_of_days_late <= 10 :
            fine = (5 * 1) + ((number_of_days_late - 5) * 2)
        else:
            fine = (5 * 1) + (5 * 2) + ((number_of_days_late - 10) *5) + 10
        

    elif book_type == "childrens":
        if number_of_days_late <= 7:
            fine = number_of_days_late * 0.50
        elif number_of_days_late <= 15:
            fine = (7 * 0.50) + ((number_of_days_late - 7) * 1)
        else:
            fine = (7 * 0.50) + (8 + 1) + ((number_of_days_late -15) * 2) + 5
        
    
    elif book_type == "reference":
        fine = (number_of_days_late * 10) + 20
    print(f"Your total fine is: ${fine}")


