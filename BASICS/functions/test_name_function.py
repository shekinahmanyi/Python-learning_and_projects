
import unittest
from name_function import get_formatted_name

#We are creating a class of NamesTestCase which will contain a series of unit tests for the function get_formatted_name.
# The class inherits from unittest.TestCase, which provides a framework for writing and running tests.
# The test case is designed to check if the function correctly formats names by capitalizing the first letter of each name.
class NamesTestCase(unittest.TestCase): 
    """Tests for 'name_function.py'."""
    def test_first_last_name(self): ## Test for a standard first and last name.
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin') #We call the fxn with any first and last name we will love to test.
        # The assertEqual method is used to check if the output of the function matches the expected output.
        # If they match, the test passes; if not, it fails.
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
 
if __name__ == '__main__': ## This line checks if the script is being run directly (not imported as a module).
    # If it is, it calls unittest.main(), which runs all the test cases defined in the script.
    unittest.main()