#!/usr/bin/python3
""" This is a test module for testing our work"""

from console import HBNBCommand
import unittest
from models.__init__ import storage
from unittest.mock import patch
import os
import io
from uuid import UUID
from models.state import State
from models.place import Place


class TestConsole(unittest.TestCase):
    """Test the console module"""

    def setUp(self):
        """The setup for console testing"""
        # Test file for json
        pass

    def tearDown(self):
        """The Tear down for console testing
        functions at the end of each test"""

        # Remove test file after each test
        os.system('rm -f file.json')

    def test_show(self):
        """Test the help show functionality"""

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help show")

            # Retrieve the captured output
            output = f.getvalue().strip()
            self.assertEqual("Shows an individual instance of a " +
                             "class\n[Usage]:" +
                             " show <className> <objectId>", output)

    def test_create_ordinary(self):
        """Test the create method of cmd"""

        output = ''
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')

            # Retrieve the captured output
            output = f.getvalue().strip()

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('show State {}'.format(output))
            output = f.getvalue().strip()
            self.assertIn("\'name\': \'California\'", output)

    def test_create_apostrophe(self):
        """Test the create method of cmd"""

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name=\"Califor"nia\"')

            # Retrieve the captured output
            output = f.getvalue().strip()
            self.assertTrue(UUID(output))

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('show State {}'.format(output))
            output = f.getvalue().strip()
            self.assertNotIn("\'name\': \'California\'", output)

    def test_create_int_float_combine(self):
        """Test the create method of cmd"""

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create Place city_id=\"0001\" ' +
                                 'user_id=\"0001\"  name=\"My_little_house\"' +
                                 ' number_rooms=4 number_bathrooms=2 ' +
                                 'max_guest=10 price_by_night=300' +
                                 ' latitude=37.773972 longitude=-122.431297')

            # Retrieve the captured output
            output = f.getvalue().strip()
            self.assertTrue(UUID(output))

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('show Place {}'.format(output))
            output = f.getvalue().strip()
            self.assertIn("\'city_id\': \'0001\'", output)
            self.assertIn("\'number_rooms\': 4", output)

    def test_create_space_for_underscore(self):
        """Test the create method of cmd"""

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name=\"Cali for nia\"')

            # Retrieve the captured output
            output = f.getvalue().strip()
            self.assertTrue(UUID(output))

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('show State {}'.format(output))
            output = f.getvalue().strip()
            self.assertNotIn("\'name\': \'California\'", output)

    def test_create_apostrophe2(self):
        """Test the create method of cmd"""

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create State name=\'California\'")

            # Retrieve the captured output
            output = f.getvalue().strip()
            self.assertTrue(UUID(output))

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('show State {}'.format(output))
            output = f.getvalue().strip()
            self.assertNotIn("\'name\': \'California\'", output)

    def test_create_wrong_int(self):
        """Test the create method of cmd"""

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name=5t')

            # Retrieve the captured output
            output = f.getvalue().strip()
            self.assertTrue(UUID(output))

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('show State {}'.format(output))
            output = f.getvalue().strip()
            self.assertNotIn("\'name\': 5t", output)

    def test_create_wrong_float(self):
        """Test the create method of cmd"""

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name=5.333\"')

            # Retrieve the captured output
            output = f.getvalue().strip()
            self.assertTrue(UUID(output))

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('show State {}'.format(output))
            output = f.getvalue().strip()
            self.assertNotIn("\'name\': 5.333\"", output)


if __name__ == '__main__':
    unittest.main()
