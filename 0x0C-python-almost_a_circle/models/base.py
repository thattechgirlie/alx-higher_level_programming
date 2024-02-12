#!/usr/bin/python3
"""Defining base model."""
import json
import csv
import turtle


class Base:
    """Base model.
    Represents the "base" for all other classes in almost a circle project.
    Private Class Attributes:
        __nb_object (int): Number of indtantiated Bases.
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """Initialize new Base.
        Args:
            id (int): Identity of new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON list of dictionaries.
        Args:
            list_dictionaries (list): List of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
                return "[]"
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON of list of objects to file.
        Args:
            list_objs (list): List of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return deserialization of JSONstring.
        Args:
            json_string (str): JSON string representing list of dictionaries.
            Returns:
                If json_string is None or empty - empty list.
                Otherwise - python list is represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return class instance from dictionary of attributes.
        Args:
            **dictionary (dict): Key pairs of attributes to initalize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return list of class instances from JSON string files.
        Read from `<cls.__name__>.json`.
        Returns:
            If file does not exist - empty list.
            Otherwise - list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_filecsv(cls, list_objs):
        """Write CSV serialization list of objects to a file.
        Args:
            list_objs (list): List of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return list of classes instatiated from CSV file.
        Read from `<cls.__name__>.csv`.

        Returns:
            If file does not exist - empty list./
            Otherwise - list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(a)] for k, a in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
