
import unittest
from user import Credentials, User


class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the Users class behaviours.
    """
    def setUp(self):
        '''
        method to run each test
        '''
        self.user = User("Barry", "Barry@1234")

    def test_init(self):
        '''
        Test to check proper user initialization
        '''
        self.assertEqual(self.user.username, "Barry")
        self.assertEqual(self.user.password, "Barry@1234")

    def test_save_multiple_users(self):
        '''
        method to test multiple saved users
        '''
        self.user.saveUser()
        test_user = User("Juma", "Juma") 
        test_user.saveUser()

        self.assertEqual(len(User.userList), 2)

    def tearDown(self):
        '''
        method to clean up after each test
        '''

        User.userList = []

    
    def test_delete_user(self):
        """
        method to test delete users
        """
        self.user.saveUser()
        test_user = User("Juma", "Juma") 
        test_user.saveUser()

        self.user.deleteUser()
        self.assertEqual(len(User.userList), 1)

    def test_display_users(self):
        """
        method to test if users are correctly displayed
        """
        self.assertEqual(User.displayUser(), User.userList)

class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        Method to define the constructor
        """
        self.cred = Credentials("email", "Barry@1234", "Barry")

    def test_init(self):
        """
        make sure the credential is well initialized
        """
        self.assertEqual(self.cred.username, "Barry")
        self.assertEqual(self.cred.account, "email")
        self.assertEqual(self.cred.password, "Barry@1234")

    def tearDown(list):
        """
        clear up during each test
        """
        Credentials.credentials = []

    def test_save_multiples_credential(self):
        """
        test for multiple credentials
        """
        self.cred.saveCredential()
        test_cred = Credentials("email", "Barry", "Barry@1234") 
        test_cred.saveCredential()

        self.assertEqual(len(Credentials.credentials), 2)

    def test_delete(self):
        """
        test to delete credentials
        
        """
        self.cred.saveCredential()
        test_cred = Credentials("email", "Barry", "Barry@1234") 
        test_cred.saveCredential()

        self.cred.deleteCredential()
        self.assertEqual(len(Credentials.credentials), 2)

  

if __name__ == "__main__":
    unittest.main() 