"""
    https://realpython.com/python-f-strings/
    # * Before Python 3.6
    # ? string interpolation operator (%)
    # ? str.format() method
"""

# MODULO OPERATOR (%)
#####################

"""
     _________________________
    | Especificador | Formato |
    |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|¯¯¯¯¯¯¯¯¯|
    | %s            | Cadena  |
    | %d            | Entero  |
    | %o            | Octal   |
    | %x            | Hexa    |
    | %f            | Real    |
    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
"""

# ***
name = "Jane"
print("Hello, %s!" % name)

# ***
name = "Jane"
age = 25

print("Hello, %s! You're %s years old." % (name, age))

# ***
print("Hello, %(name)s! You're %(age)s years old." % {"name": "Jane", "age": 25})

# ***
print("Balance: $%.2f" % 5425.9292)

print("Name: %s\nAge: %5s" % ("Jhon", 35))

# ***
# print("The personal info is: %s" % ("Jhon", 35)) # ! TypeError: not all arguments converted during string formatting

print("The personal info is: %s" % (("Jhon", 35),))

# str.format() Method
#####################

name = "Jane"
age = 25

# ***
print("Hello, {}! You're {} years old.".format(name, age))

print("Hello, {1}! You're {0} years old.".format(age, name))

# ***
print("Hello, {name}! You're {age} years old.".format(name="Jane", age=25))

# ***
person = {"name": "Jane", "age": 25}

print("Hello, {name}! You're {age} years old.".format(**person))

# ***
print("Balance: ${:.2f}".format(5425.9292))

print("{:=^30}".format("Centered string"))
print("{:=<30}".format("Left string"))
print("{:=>30}".format("Right string"))

# F-Strings
#####################

name = "Jane"
age = 25

print(f"Hello, {name}! You're {age} years old.")

# ***
print(f"{2 * 21}")

# ***
name = "Jane"
age = 25

print(f"Hello, {name.upper()}! You're {age} years old.")

print(f"{[2**n for n in range(3, 9)]}")

# ***
print(format(5425.9292, ".2f"))

# ***
balance = 5425.9292

print(f"Balance: ${balance:.2f}")

heading = "Centered string"
print(f"{heading:=^30}")

# ***
