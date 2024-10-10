# Controlling the Object Creation Process
## Initializing Objexts with .__init__()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(21, 42)
print(point.x)
print(point.y)

## Creating Objects With .__new__()
class Storage(float):
    def __new__(cls, value, unit):
        instance = super().__new__(cls, value)
        instance.unit = unit
        return instance

disk = Storage(1024, "GB")
print(disk)
print(disk.unit)
print(isinstance(disk, float))

# Representing Objects as Strings
## User-Friendly String Representations With .__str__()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"I'm {self.name}, and I'm {self.age} years old."

    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', age={self.age})"

jane = Person("Jane Doe", 25)
print(str(jane))
print(jane)

## Developer-Friendly String Representations With .__repr__()
john = Person("John Doe", 35)
print(john)
print(repr(john))

# Supporting Operator Overloading in Custom Classes
## Arithmetic Operators

# Operator	| Supporting Method
# ----------|------------------------------------
# +	        | .__add__(self, other)
# -	        | .__sub__(self, other)
# *	        | .__mul__(self, other)
# /	        | .__truediv__(self, other)
# //	    |     .__floordiv__(self, other)
# %	        | .__mod__(self, other)
# **	    |     .__pow__(self, other[, modulo])

class Storage(float):
    def __new__(cls, value, unit):
        instance = super().__new__(cls, value)
        instance.unit = unit
        return instance

    def __add__(self, other):
            if not isinstance(other, type(self)):
                raise TypeError(
                    "unsupported operand for +: "
                    f"'{type(self).__name__}' and '{type(other).__name__}'"
                )
            if not self.unit == other.unit:
                raise TypeError(
                    f"incompatible units: '{self.unit}' and '{other.unit}'"
                )

            return type(self)(super().__add__(other), self.unit)

    def __sub__(self, other):
            if not isinstance(other, type(self)):
                raise TypeError(
                    "unsupported operand for -: "
                    f"'{type(self).__name__}' and '{type(other).__name__}'"
                )
            if not self.unit == other.unit:
                raise TypeError(
                    f"incompatible units: '{self.unit}' and '{other.unit}'"
                )

            return type(self)(super().__sub__(other), self.unit)

disk_1 = Storage(500, "GB")
disk_2 = Storage(1000, "GB")
disk_3 = Storage(1, "TB")
print(disk_1 + disk_2)
print(disk_2 + disk_3)
print(disk_1 + 100)

class Distance:
    _multiples = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1_000,
    }

    def __init__(self, value, unit="m"):
        self.value = value
        self.unit = unit.lower()

    def to_meter(self):
        return self.value * type(self)._multiples[self.unit]

    def __add__(self, other):
        return self._compute(other, "+")

    def __sub__(self, other):
        return self._compute(other, "-")

    def _compute(self, other, operator):
        operation = eval(f"{self.to_meter()} {operator} {other.to_meter()}")
        cls = type(self)
        return cls(operation / cls._multiples[self.unit], self.unit)

distance_1 = Distance(200, "m")
distance_2 = Distance(1, "km")

total = distance_1 + distance_2
print(total.value)
print(total.unit)

displacement = distance_2 - distance_1
print(displacement.value)
print(displacement.unit)

## More on Arithmetic Operators
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print("__add__ called")
        if isinstance(other, Number):
            return Number(self.value + other.value)
        elif isinstance(other, int | float):
            return Number(self.value + other)
        else:
            raise TypeError("unsupported operand type for +")

    def __radd__(self, other):
        print("__radd__ called")
        return self.__add__(other)

five = Number(5)
ten = Number(10)
fifteen = five + ten
print(fifteen.value)

six = five + 1
print(six.value)

twelve = 2 + ten
print(twelve.value)

# Operator	| Right-Hand Method
# ----------|-------------------------------
# +	        | .__radd__(self, other)
# -	        | .__rsub__(self, other)
# *	        | .__rmul__(self, other)
# /	        | .__rtruediv__(self, other)
# //	    | .__rfloordiv__(self, other)
# %	        | .__rmod__(self, other)
# **	    | .__rpow__(self, other[, modulo])

# Operator	| Supporting Method	| Description
# ----------|-------------------|-----------------------------------------------------------------------------
# -	        | .__neg__(self)	| Returns the target value with the opposite sign
# +	        | .__pos__(self)	| Provides a complement to the negation without performing any transformation

## Comparison Operator Methods

# Operator | Supporting Method
# ---------|---------------------
# <	       | .__lt__(self, other)
# <=	   | .__le__(self, other)
# ==	   | .__eq__(self, other)
# !=	   | .__ne__(self, other)
# >=	   | .__ge__(self, other)
# >	       | .__gt__(self, other)

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

basketball_court = Rectangle(15, 28)
soccer_field = Rectangle(75, 110)
print(basketball_court < soccer_field)
print(basketball_court > soccer_field)
print(basketball_court == soccer_field)

## Membership Operators

print(2 in [2, 3, 5, 9, 7])
print(10 in [2, 3, 5, 9, 7])

class Stack:
    def __init__(self, items=None):
        self.items = list(items) if items is not None else []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __contains__(self, item):
        for current_item in self.items:
            if item == current_item:
                return True
        return False

    # * More concise
    # def __contains__(self, item):
    #     return item in self.items
stack = Stack([2, 3, 5, 9, 7])

print(2 in stack)
print(10 in stack)
print(2 not in stack)
print(10 not in stack)

## Bitwise Operators

# Operator	| Supporting Method
# ----------|---------------------
# &	        | .__and__(self, other)
# |	        | .__or__(self, other)
# ^	        | .__xor__(self, other)
# <<	    | .__lshift__(self, other)
# >>	    | .__rshift__(self, other)
# ~	        | .__invert__()

class BitwiseNumber:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        return type(self)(self.value & other.value)

    def __or__(self, other):
        return type(self)(self.value | other.value)

    def __xor__(self, other):
        return type(self)(self.value ^ other.value)

    def __invert__(self):
        return type(self)(~self.value)

    def __lshift__(self, places):
        return type(self)(self.value << places)

    def __rshift__(self, places):
        return type(self)(self.value >> places)

    def __repr__(self):
        return bin(self.value)

five = BitwiseNumber(5)
ten = BitwiseNumber(10)

# Bitwise AND
#    0b101
# & 0b1010
# --------
#      0b0
print(five & ten)

# Bitwise OR
#    0b101
# | 0b1010
# --------
#   0b1111
print(five | ten)
print(five ^ ten)
print(~five)
print(five << 2)
print(ten >> 1)

## Augmented Assignments
counter = 0
counter = counter + 1
counter = counter + 1
print(counter)

counter = 0
counter += 1
counter += 1
print(counter)

# Operator	| Supporting Method
# ----------|------------------------
# +=	    | .__iadd__(self, other)
# -=	    | .__isub__(self, other)
# *=	    | .__imul__(self, other)
# /=	    | .__itruediv__(self, other)
# //=	    | .__ifloordiv__(self, other)
# %=	    | .__imod__(self, other)
# **=	    | .__ipow__(self, other[, modulo])

class Stack:
    def __init__(self, items=None):
        self.items = list(items) if items is not None else []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __contains__(self, item):
        for current_item in self.items:
            if item == current_item:
                return True
        return False

    def __add__(self, other):
        return type(self)(self.items + other.items)

    def __iadd__(self, other):
        self.items.extend(other.items)
        return self

    def __repr__(self):
        return f"{type(self).__name__}({self.items!r})"

stack = Stack([1, 2, 3])
stack += Stack([4, 5, 6])
print(stack)

# Operator	| Supporting Method
# ----------|-------------------
# &=	    | .__iand__(self, other)
# |=	    | .__ior__(self, other)
# ^=	    | .__ixor__(self, other)
# <<=	    | .__ilshift__(self, other)
# >>=	    | .__irshift__(self, other)

# Introspecting Your Objects

# Method	           | Description
# ---------------------|---------------------------------------------------------------
# .__dir__()	       | Returns a list of attributes and methods of an object
# .__hasattr__()	   | Checks whether an object has a specific attribute
# .__instancecheck__() | Checks whether an object is an instance of a certain class
# .__subclasscheck__() | Checks whether a class is a subclass of a certain class

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __dir__(self):
        print("__dir__ called")
        return sorted(self.__dict__.keys())

dir(Rectangle(12, 24))

# Controlling Attribute Access

# Method	                        | Description
# ----------------------------------|-----------------------------------------------------------------------------
# .__getattribute__(self, name)	    | Runs when you access an attribute called name
# .__getattr__(self, name)	        | Runs when you access an attribute that doesn’t exist in the current object
# .__setattr__(self, name, value)	| Runs when you assign value to the attribute called name
# .__delattr__(self, name)	        | Runs when you delete the attribute called name

## Retrieving Attributes
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __getattribute__(self, name):
        print(f"__getattribute__ called for {name}")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print(f"__getattr__ called for {name}")
        if name == "diameter":
            return self.radius * 2
        return super().__getattr__(name)

circle = Circle(10)
print(circle.radius)
print(circle.diameter)

## Setting Attributes
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __getattribute__(self, name):
        print(f"__getattribute__ called for {name}")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print(f"__getattr__ called for {name}")
        if name == "diameter":
            return self.radius * 2
        return super().__getattr__(name)
    
    def __setattr__(self, name, value):
        if name == "radius":
            if not isinstance(value, int | float):
                raise TypeError("radius must be a number")
            if value <= 0:
                raise ValueError("radius must be positive")
        super().__setattr__(name, value)

circle = Circle(10)
circle.radius = 20
circle.radius = "42"
circle.diameter = 42
print(circle.diameter)

## Deleting Attributes

class NonDeletable:
    def __init__(self, value):
        self.value = value

    def __delattr__(self, name):
        raise AttributeError(
            f"{type(self).__name__} doesn't support attribute deletion"
        )

one = NonDeletable(1)
print(one.value)
del one.value

# Managing Attributes Through Descriptors

# Method	                                | Description
# ------------------------------------------|-------------------------------------------------------------------------------------
# .__get__(self, instance, type=None)	    | Getter method that allows you to retrieve the current value of the managed attribute
# .__set__(self, instance, value)	        | Setter method that allows you to set a new value to the managed attribute
# .__delete__(self, instance)	            | Deleter method that allows you to remove the managed attribute from the containing class
# .__set_name__(self, owner, name)	        | Name setter method that allows you to define a name for the managed attribute

class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        instance.__dict__[self._name] = value

import math

class Circle:
    radius = PositiveNumber()

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius**2, 2)

class Square:
    side = PositiveNumber()

    def __init__(self, side):
        self.side = side

    def area(self):
        return round(self.side**2, 2)

class Rectangle:
    height = PositiveNumber()
    width = PositiveNumber()

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

circle = Circle(-10)
square = Square(-20)
rectangle = Rectangle(-20, 30)

# Supporting Iteration With Iterators and Iterables
## Creating Iterators

# Method    	| Description
# --------------|------------------------------------------------------------------------------------------
# .__iter__()	| Called to initialize the iterator. It must return an iterator object.
# .__next__()	| Called to iterate over the iterator. It must return the next value in the data stream.

class FibonacciIterator:
    def __init__(self, stop=10):
        self._stop = stop
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._stop:
            self._index += 1
            fib_number = self._current
            self._current, self._next = (
                self._next,
                self._current + self._next,
            )
            return fib_number
        else:
            raise StopIteration

for fib_number in FibonacciIterator():
    print(fib_number)

## Building Iterables

class Stack:
    def __init__(self, items=None):
        self.items = list(items) if items is not None else []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __contains__(self, item):
        for current_item in self.items:
            if item == current_item:
                return True
        return False

    def __add__(self, other):
        return type(self)(self.items + other.items)

    def __iadd__(self, other):
        self.items.extend(other.items)
        return self

    def __repr__(self):
        return f"{type(self).__name__}({self.items!r})"

    def __iter__(self):
        return iter(self.items[::-1])

stack = Stack([1, 2, 3, 4])
for value in stack:
    print(value)

# Making Your Objects Callable

class Factorial:
    def __init__(self):
        self._cache = {0: 1, 1: 1}

    def __call__(self, number):
        if number not in self._cache:
            self._cache[number] = number * self(number - 1)
        return self._cache[number]

factorial_of = Factorial()
print(factorial_of(4))
print(factorial_of(5))
print(factorial_of(6))

# Implementing Custom Sequences and Mappings

# Method	        | Description
# ------------------|-----------------------------------------------------------------------------------------------------------
# .__getitem__()	| Called when you access an item using indexing like in sequence[index]
# .__len__()	    | Called when you invoke the built-in len() function to get the number of items in the underlying sequence
# .__contains__()	| Called when you use the sequence in a membership test with the in or not in operator
# .__reversed__()	| Called when you use the built-in reversed() function to get a reversed version of the underlying sequence

class Stack:
    def __init__(self, items=None):
        self.items = list(items) if items is not None else []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __contains__(self, item):
        for current_item in self.items:
            if item == current_item:
                return True
        return False

    def __add__(self, other):
        return type(self)(self.items + other.items)

    def __iadd__(self, other):
        self.items.extend(other.items)
        return self

    def __repr__(self):
        return f"{type(self).__name__}({self.items!r})"

    def __iter__(self):
        return iter(self.items[::-1])

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)

    def __reversed__(self):
        return type(self)(reversed(self.items))

stack = Stack([1, 2, 3, 4])
print(stack[1])
print(stack[-1])
print(len(stack))
print(reversed(stack))

# Handling Setup and Teardown With Context Managers

with open("resources/hello.txt", mode="w", encoding="utf-8") as file:
   file.write("Hello, World!")

with open("hello.txt", mode="r", encoding="utf-8") as file:
    print(file.read())

# Method	    | Description
# --------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# .__enter__()	| Sets up the runtime context, acquires resources, and may return an object that you can bind to a variable with the as specifier on the with header
# .__exit__()	| Cleans up the runtime context, releases resources, handles exceptions, and returns a Boolean value indicating whether to propagate any exceptions that may occur in the context

class TextFileReader:
    def __init__(self, file_path, encoding="utf-8"):
        self.file_path = file_path
        self.encoding = encoding

    def __enter__(self):
        self.file_obj = open(self.file_path, mode="r", encoding=self.encoding)
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()

with TextFileReader("resources/hello.txt") as file:
    print(file.read())