#!/usr/bin/python3
"""
task 10
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ constructor """
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """ string """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size """
        self.width = value
        self.height = value
    def update(self, *args, **kwargs):
        """ update """
        attributes = ["id", "size", "x", "y"]

        if args:
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Dictionary """
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
