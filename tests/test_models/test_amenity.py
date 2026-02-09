#!/usr/bin/python3
"""Unittests for Amenity class."""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_instance(self):
        """Test that an Amenity instance can be created."""
        instance = Amenity()
        self.assertIsNotNone(instance)

    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
