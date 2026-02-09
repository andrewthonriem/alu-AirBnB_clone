#!/usr/bin/python3
"""Unittests for User class."""

import unittest
from datetime import datetime
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_attributes_exist(self):
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_default_values(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_inheritance(self):
        user = User()
        from models.base_model import BaseModel
        self.assertIsInstance(user, BaseModel)

    def test_to_dict_contains_class(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIn("__class__", user_dict)
        self.assertEqual(user_dict["__class__"], "User")

    def test_save_and_reload(self):
        user = User()
        user.first_name = "Betty"
        user.email = "test@mail.com"
        user.save()
        user_id = user.id
        # Clear __objects to simulate reload
        storage.__dict__['FileStorage__objetcs'] = {}
        storage.reload()
        all_objs = storage.all()
        key = f"User.{user_id}"
        self.assertIn(key, all_objs)
        reloaded_user = all_objs[key]
        self.assertEqual(reloaded_user.first_name, "Betty")
        self.assertEqual(reloaded_user.email, "test@mail.com")


if __name__ == "__main__":
    unittest.main()
