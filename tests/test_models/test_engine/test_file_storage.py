#!/usr/bin/python3
"""Unittests for FileStorage class."""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Clean up before each test."""
        self.file_path = "file.json"
        # Clear objects and remove file if exists
        storage.__dict__['FileStorage__objetcs'] = {}
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        storage.__dict__['FileStorage__objetcs'] = {}

    def test_instance_creation(self):
        """Test that FileStorage instance can be created."""
        self.assertIsNotNone(self.storage)

    def test_new_and_all(self):
        """Test adding a new object and checking all()"""
        model = BaseModel()
        self.storage.new(model)
        all_objs = self.storage.all()
        key = f"BaseModel.{model.id}"
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key], model)

    def test_save_creates_file(self):
        """Test that save() writes JSON file correctly."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, "r") as f:
            data = f.read()
            self.assertIn(model.id, data)
            self.assertIn("BaseModel", data)

    def test_reload_restores_objects(self):
        """Test that reload() restores objects from JSON file."""
        model = BaseModel()
        key = f"BaseModel.{model.id}"
        self.storage.new(model)
        self.storage.save()

        # Clear __objects and reload
        storage.__dict__['FileStorage__objetcs'] = {}
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn(key, all_objs)
        restored = all_objs[key]
        self.assertEqual(restored.id, model.id)
        self.assertEqual(restored.created_at, model.created_at)
        self.assertEqual(restored.updated_at, model.updated_at)


if __name__ == "__main__":
    unittest.main()
