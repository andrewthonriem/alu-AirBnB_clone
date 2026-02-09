#!/usr/bin/python3
"""
BaseModel class defines all common attributes/methods for other classes.
Public attributes: {"id(uuid.uuid4)", "created_at", "updated_at"}
Public instance methods: {"save(self)", "to_dict"}
"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

            from models import storage
            storage.new(self)

    def __str__(self):
        """Return the string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()  # update the file

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        return {
            **self.__dict__,
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
