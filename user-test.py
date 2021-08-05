import unittest
from user import user
from user import credentials

class TestClass(unittest.TestCase):
        
        def setUp(self):
                self.new_user= user("Barry", "Barry@1234")
        def test_init(self):
                self.assertEqual =(self.newName,"Barry")
                self.assertEqual =(self.newName,"Barry@1234")
	    