num1 = int(input("Enter your fisrt integer: "))
num2 = int(input("Enter your second integer: "))

symbol = input("Enter any symbol to print your answer: ")

match symbol:
    case "+":
        print(f"The sum of your two intergers are", num1 + num2)

    case "-":
        print(f"The substraction of your two intergers are", num1 - num2)

    case "*":
        print(f"The multiplication of your two intergers are", num1 * num2)

    case "**":
        print(f"The exponential of your two intergers are", num1 ** num2)

    case "/":
        print(f"The division of your two intergers are", num1 / num2)

    case "%":
        print(f"The modules of your two intergers are", num1 % num2)

    case "//":
        print(f"The floor division of your two intergers are", num1 + num2)

    case _:
        print("Invalid symbol")



# Create a variable day with the value 3
# Use a match statement to check the value of day
# Add a case 3 that prints "Wednesday"
# Add a wildcard case _ that prints "Other day"

day = 3

match day:
    case 3:
        print("Wednesday")

    case _:
        print("Other day")

        
