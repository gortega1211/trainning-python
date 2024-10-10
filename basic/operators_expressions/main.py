print(-273.15)
print(5 - 2)

print(42 == 42)

# print(-)
# print(==)
# print(or)

print(7 + 5)
print(42 / 2)
print(5 == 5)

print(abs(-7))
print(pow(2, 8))
print("Hello World!")

number = 42
day = "Friday"
digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
letters = ["a", "b", "c"]

a = 5
b = 2
print(+a)
print(-b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)

print(10 / 5)
print(10.0 / 5)
print(10 / 5j)
print(10 // 4)
print(-10 // -4)
print(10 // -4)
print(-10 // 4)

print(2 == "2")
print(5 < "7")

a = 10
b = 20
print(a == b)
print(a != b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)

x = 30
y = 30
print(x == y)
print(x != y)
print(x < y)
print(x <= y)
print(x > y)
print(x >= y)

x = 1.1 + 2.2
print(x == 3.3)
print(1.1 + 2.2)

from math import isclose
x = 1.1 + 2.2
isclose(x, 3.3)

print(ord("A"))
print(ord("a"))
print("A" == "a")
print("A" > "a")
print("A" < "a")
print("Hello" > "HellO")
print(ord("o"))
print(ord("O"))
print("Hello" > "Hello, World!")

print([2, 3] == [2, 3])
print((2, 3) == (2, 3))
print([5, 6, 7] < [7, 5, 6])
print((5, 6, 7) < (7, 5, 6))
print([4, 3, 2] < [4, 3, 2])
print((4, 3, 2) < (4, 3, 2))
print([2, 3] == (2, 3))
print([2, 3] != (2, 3))
print([2, 3] > (2, 3))
print([2, 3] <= (2, 3))

print([5, 6, 7] < [8])
print((5, 6, 7) < (8,))
print([5, 6, 7] == [5])
print((5, 6, 7) == (5,))
print([5, 6, 7] > [5])
print((5, 6, 7) > (5,))

age = 20
is_adult = age > 18
print(is_adult)
print(type(is_adult))

number = 42
validation_conditions = (
    isinstance(number, int),
    number % 2 == 0,
)
print(all(validation_conditions))
print(callable(number))
print(callable(print))

print(5 < 7 and 3 == 3)
print(5 < 7 and 3 != 3)
print(5 > 7 and 3 == 3)
print(5 > 7 and 3 != 3)
print(5 < 7 or 3 == 3)
print(5 < 7 or 3 != 3)
print(5 > 7 or 3 == 3)
print(5 > 7 or 3 != 3)
print(5 < 7)
print(not 5 < 7)

print(bool(0), bool(0.0), bool(0.0+0j))
print(bool(-3), bool(3.14159), bool(1.0+1j))
print(bool(""))
print(bool(" "))
print(bool("Hello"))
print(bool([]))
print(bool([1, 2, 3]))
print(bool(()))
print(bool(("John", 25, "Python Dev")))
print(bool(set()))
print(bool({"square", "circle", "triangle"}))
print(bool({}))
print(bool({"name": "John", "age": 25, "job": "Python Dev"}))

print(3 and 4)
print(0 and 4)
print(3 and 0)
print(3 or 4)
print(0 or 4)
print(3 or 0)
print(0 or [])
print(not 3)
print(not 0)

def f(arg):
    print(f"-> f({arg}) = {arg}")
    return arg

print(f(0))
print(f(False))
print(f(1.5))
print(f(0) or f(False) or f(1) or f(2) or f(3))
print(f(1) and f(False) and f(2) and f(3))
print(f(1) and f(0.0) and f(2) and f(3))
print(f(1) and f(2.2) and f("Hello"))
print(f(1) and f(2.2) and f(0))

a = 3
b = 1
print(b / a > 0)
a = 0
b = 1
print(b / a > 0)
a = 0
b = 1
print(a != 0 and (b / a) > 0)
def is_divisible(a, b):
    return b != 0 and a % b == 0
country = "Canada"
default_country = "United States"
print(country or default_country)
country = ""
print(country or default_country)

number = 5
print(number >= 0 and number <= 10)
number = 42
print(number >= 0 and number <= 10)
number = 5
print(0 <= number <= 10)

day = "Sunday"
open_time = "11AM" if day == "Sunday" else "9AM"
print(open_time)
day = "Monday"
open_time = "11AM" if day == "Sunday" else "9AM"
print(open_time)

x = 1001
y = 1001
print(x == y)
print(x is y)
print(id(x))
print(id(y))
a = "Hello, Pythonista!"
b = a
print(id(a))
print(id(b))
print(a is b)
x = 1001
y = 1001
print(x is not y)
a = "Hello, Pythonista!"
b = a
print(a is not b)

print(5 in [2, 3, 5, 9, 7])
print(8 in [2, 3, 5, 9, 7])
print(5 not in [2, 3, 5, 9, 7])
print(8 not in [2, 3, 5, 9, 7])

print("Hello, " + "World!")
print(("A", "B", "C") + ("D", "E", "F"))
print([0, 1, 2, 3] + [4, 5, 6])
print("Hello" * 3)
print(3 * "World!")
print(("A", "B", "C") * 3)
print(3 * [1, 2, 3])

def validate_length(string):
    if (n := len(string)) < 8:
        print(f"Length {n} is too short, needs at least 8")
    else:
        print(f"Length {n} is okay!")
validate_length("Pythonista")
validate_length("Python")

# Bitwise AND
#   0b1100    12
# & 0b1010    10
# --------
# = 0b1000     8
print(bin(0b1100 & 0b1010))
print(12 & 10)
# Bitwise OR
#   0b1100    12
# | 0b1010    10
# --------
# = 0b1110    14
print(bin(0b1100 | 0b1010))
print(12 | 10)

# Operators	        | Description
# ------------------|-------------------------------------------------
# **	            | Exponentiation
# ------------------|-------------------------------------------------
# +x, -x, ~x	    | Unary positive, unary negation, bitwise negation
# ------------------|-------------------------------------------------
# *, /, //, %	    | Multiplication, division, floor division, modulo
# ------------------|-------------------------------------------------
# +, -	            | Addition, subtraction
# ------------------|-------------------------------------------------
# <<, >>	        | Bitwise shifts
# ------------------|-------------------------------------------------
# &	                | Bitwise AND
# ------------------|-------------------------------------------------
# ^	                | Bitwise XOR
# ------------------|-------------------------------------------------
# |	                | Bitwise OR
# ------------------|-------------------------------------------------
# ==, !=, <, <=, >, |
# >=, is, is not,   | Comparisons, identity, and membership
# in, not in	    |
# ------------------|-------------------------------------------------
# not	            | Boolean NOT
# ------------------|-------------------------------------------------
# and	            | Boolean AND
# ------------------|-------------------------------------------------
# or	            | Boolean OR
# ------------------|-------------------------------------------------
# :=	            | Walrus
# ------------------|-------------------------------------------------
print(20 + 4 * 10)
print(2 * 3 ** 4 * 5)
print((20 + 4) * 10)
print(2 * 3 ** (4 * 5))

total = 10
total = total + 5
print(total)
count = count + 1
total = 10
total += 5
print(total)