#!/usr/bin/python3
"""
task 2
"""


from models.base import Base
class Rectangle(Base):
    """ rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        self.validate_integer("width", value, 1)
        self.__width = value

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        self.validate_integer("height", value, 1)
        self.__height = value

    @property
    def x(self):
        """ get x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set x """
        self.validate_integer("x", value, 0)
        self.__x = value

    @property
    def y(self):
        """ get y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set y """
        self.validate_integer("y", value, 0)
        self.__y = value

    def validate_integer(self, name, value, flag=1):
        """ validate value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if flag == 0 and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif flag == 1 and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """ area of rectangle """
        return self.width * self.height

    def display(self):
        """ Display the rectangle using '#' character """
        for _ in range(self.y):
            print()  

        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)


    def __str__(self):
        """  overriding the __str__ method """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args):
        """ update """
        attributes = ["id", "width", "height", "x", "y"]
        for i, value in enumerate(args):
            setattr(self, attributes[i], value)


    def update(self, *args, **kwargs):
        """ update """
        attributes = ["id", "width", "height", "x", "y"]

        if args:
            # If positional arguments exist, use them
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        else:
            # If no positional arguments, use keyword arguments
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)


    def to_dictionary(self):
        """ Dictionary """
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
