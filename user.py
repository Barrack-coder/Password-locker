import unittest
from user import user
from user import credentials

class TestClass(unittest.TestCase):
        
        def setUp(self):
	    #method used to run the test
	           self.new_user("Barry","Barry@123")
        