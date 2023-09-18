0x0C-python-almost_a_circle

-Write the first class Base:
Create a folder named models with an empty file
__init__.py inside - with this file, the folder will become a Python package
Create a file named models/base.py:
Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute id with this
argument value - you can assume id is an integer and you don’t need to
test the type of it
otherwise, increment __nb_objects and assign the new value to the
public instance attribute id.

-Write the class Rectangle that inherits from Base:
In the file models/rectangle.py
Class Rectangle inherits from Base
Private instance attributes, each with its own public getter
and setter:
__width -> width
__height -> height
__x -> x
__y -> y
Class constructor:
def __init__(self, width, height, x=0, y=0, id=None):
Call the super class with id - this super call with use the logic
of the __init__ of the Base class
Assign each argument width, height, x and y to the right attribute.

-Update the class Rectangle by adding validation of all setter
methods and instantiation (id excluded):
If the input is not an integer, raise the TypeError exception with
the message: <name of the attribute> must be an integer.
Example: width must be an integer
If width or height is under or equals 0, raise the ValueError
exception with the message: <name of the attribute> must be > 0.
Example:
width must be > 0
If x or y is under 0, raise the ValueError exception with the
message: <name of the attribute> must be >= 0. Example: x must be >= 0

-Update the class Rectangle by adding the public method
def area(self): that returns the area value of the Rectangle instance.

-Update the class Rectangle by adding the public method
def display(self): that prints in stdout the Rectangle instance
with the character # - you don’t need to handle x and y here.

-Update the class Rectangle by overriding the __str__ method
so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

-Update the class Rectangle by improving the public method
def display(self): to print in stdout the Rectangle instance with the
character # by taking care of x and y

-