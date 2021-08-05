import unittest
from user import user
from user import credentials

class TestClass(unittest.TestCase):
        
        def setUp(self):
                self.new_user= user("Barry", "Barry@1234")
        def test_init(self):
                self.assertEqual =(self.newName,"Barry")
                self.assertEqual =(self.newName,"Barry@1234")
        def test_save_user(self):
                self.new_user.save_user()
                self.assertEqual (len(user.user_list),1)
class TestClass(unittest.TestCase):
        def setUp(self):
                self.assertEqual = (self.new_credentials.user,"Barry")
                self.assertEqual = (self.new_credentials.account,"email")
                self.assertEqual = (self.new_credentials.password,"Barry@1234")
	   
                           
	    