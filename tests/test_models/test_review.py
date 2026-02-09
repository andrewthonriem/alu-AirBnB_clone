#!/usr/bin/python3
"""Unittests for Review class."""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_instance(self):
        """Test that a Review instance can be created."""
        instance = Review()
        self.assertIsNotNone(instance)

    def test_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
