#!/usr/bin/python3
""" Defines a base class"""
import json
import csv


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization
        Args:
            id (int): unique id
        Returns:
        None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert object to json string"""
        if not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save object to json file"""
        if list_objs is not None:

            list_of_obj = []
            filename = cls.__name__ + '.json'

            for obj in list_objs:
                fd_dict = obj.to_dictionary()
                list_of_obj.append(fd_dict)

            with open(filename, 'w') as fd:
                json.dump(list_of_obj, fd, indent=4)

    @staticmethod
    def from_json_string(json_string):
        """Convert json string to object"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new class instance"""

        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == 'Rectangle':
            r = Rectangle(5, 10)
        elif cls.__name__ == 'Square':
            r = Square(10)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        """Load from json file and create instances with the object"""
        class_name = cls.__name__ + '.json'

        try:
            with open(class_name) as fd:
                obj = cls.from_json_string(fd.read())
        except FileNotFoundError:
            return []

        instances = []
        for i in obj:
            inst = cls.create(**i)
            instances.append(inst)

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):

        class_name = cls.__name__ + '.csv'
        with open(class_name, 'w') as fd:
            writer_obj = csv.writer(fd, delimiter=' ')

            for obj in list_objs:
                item = obj.to_dictionary()
                if cls.__name__ == 'Rectangle':

                    writer_obj.writerow(
                        [str(item['id'])] + [str(item['width'])] + [str(item['height'])] + [str(item['x'])] + [str(item['y'])])

                elif cls.__name__ == 'Square':

                    writer_obj.writerow(
                        [str(item['id'])] + [str(item['size'])] + [str(item['x'])] + [str(item['y'])])

    @classmethod
    def load_from_file_csv(cls):

        class_name = cls.__name__ + '.csv'
        list_of_obj_value = []

        with open(class_name, newline='') as fd:
            reader_ob = csv.reader(fd, delimiter=' ')

            for row in reader_ob:
                string = ''
                string += ', '.join(row)
                if string != '':
                    list_of_obj_value.append([string])

        return list_of_obj_value
