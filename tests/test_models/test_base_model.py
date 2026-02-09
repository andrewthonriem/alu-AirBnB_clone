#!/usr/bin/python3
"""Unittests for BaseModel class."""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_instance_creation(self):
        instance = BaseModel()
        self.assertIsNotNone(instance)

    def test_attributes_exist(self):
        instance = BaseModel()
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    def test_id_is_string(self):
        instance = BaseModel()
        self.assertIsInstance(instance.id, str)

    def test_created_at_is_datetime(self):
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)

    def test_updated_at_is_datetime(self):
        instance = BaseModel()
        self.assertIsInstance(instance.updated_at, datetime)

    def test_str_method(self):
        instance = BaseModel()
        string = str(instance)
        self.assertIn(instance.id, string)
        self.assertIn("BaseModel", string)

    def test_save_updates_updated_at(self):
        instance = BaseModel()
        old_time = instance.updated_at
        instance.save()
        self.assertNotEqual(old_time, instance.updated_at)

    def test_to_dict_returns_dict(self):
        instance = BaseModel()
        self.assertIsInstance(instance.to_dict(), dict)

    def test_to_dict_contains_class(self):
        instance = BaseModel()
        self.assertIn("__class__", instance.to_dict())

    def test_to_dict_datetime_are_strings(self):
        instance = BaseModel()
        dictionary = instance.to_dict()
        self.assertIsInstance(dictionary["created_at"], str)
        self.assertIsInstance(dictionary["updated_at"], str)

    def test_kwargs_reconstruction(self):
        instance = BaseModel()
        dictionary = instance.to_dict()
        new_instance = BaseModel(**dictionary)
        self.assertEqual(instance.id, new_instance.id)
        self.assertEqual(instance.created_at, new_instance.created_at)
        self.assertEqual(instance.updated_at, new_instance.updated_at)

    def test_new_object_registered_in_storage(self):
        instance = BaseModel()
        key = f"BaseModel.{instance.id}"
        self.assertIn(key, storage.all())


if __name__ == "__main__":
    unittest.main()
