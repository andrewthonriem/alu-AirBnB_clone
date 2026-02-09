#!/usr/bin/python3
"""Unit tests for console.py"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.user import User

class TestConsole(unittest.TestCase):
    """Test cases for HBNBCommand"""

    def setUp(self):
        """Clear storage before each test"""
        storage.all().clear()

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
            self.assertTrue(user_id in [obj.id for obj in storage.all().values()])

    def test_show(self):
        """Test show command"""
        user = User()
        storage.new(user)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user.id}")
            output = f.getvalue()
            self.assertIn(user.id, output)

    def test_destroy(self):
        """Test destroy command"""
        user = User()
        storage.new(user)
        storage.save()
        with patch('sys.stdout', new=StringIO()):
            HBNBCommand().onecmd(f"destroy User {user.id}")
        self.assertNotIn(f"User.{user.id}", storage.all())

    def test_all(self):
        """Test all command"""
        user = User()
        storage.new(user)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            output = f.getvalue()
            self.assertIn(user.id, output)

    def test_update_single(self):
        """Test update with single attribute"""
        user = User()
        storage.new(user)
        storage.save()
        with patch('sys.stdout', new=StringIO()):
            HBNBCommand().onecmd(f'update User {user.id} first_name "John"')
        self.assertEqual(storage.all()[f"User.{user.id}"].first_name, "John")

    def test_update_dict(self):
        """Test update with dictionary"""
        user = User()
        storage.new(user)
        storage.save()
        update_dict = '{"first_name": "Alice", "age": 30}'
        with patch('sys.stdout', new=StringIO()):
            HBNBCommand().onecmd(f"User.update(\"{user.id}\", {update_dict})")
        obj = storage.all()[f"User.{user.id}"]
        self.assertEqual(obj.first_name, "Alice")
        self.assertEqual(obj.age, 30)

    def test_count(self):
        """Test count command"""
        user1 = User()
        user2 = User()
        storage.new(user1)
        storage.new(user2)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "2")

    def test_advanced_syntax_show(self):
        """Test advanced syntax <class>.show(<id>)"""
        user = User()
        storage.new(user)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'User.show("{user.id}")')
            self.assertIn(user.id, f.getvalue())

    def test_advanced_syntax_destroy(self):
        """Test advanced syntax <class>.destroy(<id>)"""
        user = User()
        storage.new(user)
        storage.save()
        with patch('sys.stdout', new=StringIO()):
            HBNBCommand().onecmd(f'User.destroy("{user.id}")')
        self.assertNotIn(f"User.{user.id}", storage.all())

    def test_advanced_syntax_update(self):
        """Test advanced syntax <class>.update(<id>, <attr>, <value>)"""
        user = User()
        storage.new(user)
        storage.save()
        with patch('sys.stdout', new=StringIO()):
            HBNBCommand().onecmd(f'User.update("{user.id}", "last_name", "Smith")')
        obj = storage.all()[f"User.{user.id}"]
        self.assertEqual(obj.last_name, "Smith")

if __name__ == '__main__':
    unittest.main()
