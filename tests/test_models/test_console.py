#!/usr/bin/python3
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def setUp(self):
        """Set up test methods"""
        pass

    def tearDown(self):
        """Clean up after tests"""
        pass

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue().strip(), "")

    def test_help(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) > 0)


if __name__ == "__main__":
    unittest.main()
