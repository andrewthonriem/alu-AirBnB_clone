#!/usr/bin/python3
"""Unittests for City class."""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_instance(self):
        """Test that a City instance can be created."""
        instance = City()
        self.assertIsNotNone(instance)

    def test_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == "__main__":
    unittest.main()
