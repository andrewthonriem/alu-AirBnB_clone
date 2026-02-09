#!/usr/bin/python3
"""
Defines the FileStorage class for JSON
serialization and deserialization.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serialization instances to a json file and
    deserialization from json file to instances.
    """

    __file_path = "file.json"
    __objects = {}  # dictionary storing all objects

    # Class mapping
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to __objects dict
        format: <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        with open(FileStorage.__file_path, "w") as f:
            json.dump({k: v.to_dict()
                       for k, v in FileStorage.__objects.items()},
                      f, indent=4)

    def reload(self):
        """Deserialize the JSON file to __objects (if it exists)."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value.get("__class__")
                    cls = self.classes.get(class_name)
                    if cls:
                        FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
