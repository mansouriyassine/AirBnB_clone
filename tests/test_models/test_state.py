#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ Test cases for the State class """

    def test_instance_creation(self):
        """ Test creation of State instance """
        state = State()
        self.assertIsInstance(state, State)

    def test_attributes(self):
        """ Test State attributes """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
