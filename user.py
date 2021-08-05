import unittest
from user import user
from user import credentials

class TestClass(unittest.TestCase):
        
        def setUp(self):
	    #method used to run the test
	           self.new_user("Barry","Barry@123")
        def test_init(self):
                self.assertEqual = (self.new_user.userName, "Barry")
                self.assertEqual = (self.new_userPassword,"Barry@1234")
        def test_save_user(self):
                self.new_user.save_user()
                self.assertEqual (len(user.user_list),1)

        