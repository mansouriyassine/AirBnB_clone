#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ Test cases for the City class """

    def test_instance_creation(self):
        """ Test creation of City instance """
        city = City()
        self.assertIsInstance(city, City)

    def test_attributes(self):
        """ Test City attributes """
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == "__main__":
    unittest.main()
