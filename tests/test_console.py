#!/usr/bin/python3
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def test_quit(self):
        """Test the 'quit' command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual('', f.getvalue().strip())

    def test_EOF(self):
        """Test the 'EOF' command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual('', f.getvalue().strip())

    def test_help(self):
        """Test the 'help' command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue().strip()
            self.assertIn('Documented commands', output)

    def test_create(self):
        """Test the 'create' command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_show(self):
        """Test the 'show' command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertIn("** instance id missing **",
                          f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 12345")
            self.assertIn("** no instance found **",
                          f.getvalue().strip())

    def test_all(self):
        """Test the 'all' command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            output = f.getvalue().strip()
            self.assertTrue(isinstance(output, str))

    def test_update(self):
        """Test the 'update' command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                "update BaseModel 1234-1234-1234 email test@example.com")
            self.assertIn("** no instance found **",
                          f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertIn("** class name missing **",
                          f.getvalue().strip())

    def test_non_existing_command(self):
        """Test for non-existing command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("non_existing_command")
            self.assertIn("*** Unknown syntax",
                          f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
