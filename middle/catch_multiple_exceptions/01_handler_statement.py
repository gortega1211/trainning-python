try:
    first = float(input("What is your first number? "))
    second = float(input("What is your second number? "))
    print(f"{first} divided by {second} is {first / second}")
except ValueError:
    print("You must enter a number.")
except ZeroDivisionError:
    print("You can't divide by zero.")