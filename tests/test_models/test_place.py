#!/usr/bin/python3
"""Unittests for Place class."""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_instance(self):
        """Test that a Place instance can be created."""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        # Integers
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        # Floats
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        # Lists
        self.assertEqual(place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
