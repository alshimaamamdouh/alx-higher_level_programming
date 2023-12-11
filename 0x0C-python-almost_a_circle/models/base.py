#!/usr/bin/python3
"""
task 1
"""
import json
import csv



class Base:
    """ first class """
    __nb_objects = 0


    def __init__(self, id=None):
        """ constructor """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        """ jason dictionary """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)



    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"

        with open(filename, mode='w') as file:
            json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_str)
    
    


    @staticmethod
    def from_json_string(json_string):
        """ list json """
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):
        """ create """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  
        else:
            raise ValueError("Unsupported class name")

        dummy_instance.update(**dictionary)  
        return dummy_instance

    def update(self, *args, **kwargs):
        """ Assigns attributes  """
        if args:
            attrs = ['id', 'width', 'height', 'size']  
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)


    @classmethod
    def load_from_file(cls):
        """ load """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, mode='r') as file:
                json_str = file.read()
                dictionaries = cls.from_json_string(json_str)
                return [cls.create(**item) for item in dictionaries]
        except FileNotFoundError:
            return []



    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save csv """
        filename = cls.__name__ + ".csv"

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """ load csv """
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)

                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls.create(id=int(row[0]), width=int(row[1]), height=int(row[2]), x=int(row[3]), y=int(row[4]))
                    elif cls.__name__ == "Square":
                        instance = cls.create(id=int(row[0]), size=int(row[1]), x=int(row[2]), y=int(row[3]))
                    else:
                        raise ValueError("Unsupported class name")

                    instances.append(instance)

                return instances
        except FileNotFoundError:
            return []





    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
