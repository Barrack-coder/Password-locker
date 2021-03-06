           
import random
import string

class User:
    """
    Creates a user class that generates new intances of the User.
    """

    userList = []

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.isLoggedin = False
    def createUser(username, password):
        """
        Method that is used to create new user account
        """
        newUser = User(username, password)
        return newUser

    def login(self):
        """
        method that allows a user to log in after providing credentials
        """
        print("You have Successfully Logged in")

    def saveUser(self):
        """
        Method that saves a user to the list
        """
        User.userList.append(self)

    @classmethod
    def displayUser(cls):
        """
        method that displays saved users
        """
        return cls.userList

    def deleteUser(self):
        """
        method that delete a selected user
        """
        User.userList.remove(self)

if __name__ == "__main__":
    pass

class Credentials():
    """
    Method to create new user credentials
    """
    credentials = []

    def __init__(self,username ,account , password):
        """
        credentials
        """
        self.account = username
        self.username =account
        self.password = password

    def saveCredential(self):
        """
        method that adds credentials to the list
        """
        Credentials.credentials.append(self)

    @classmethod
    def createCredential(self, username, account, password):
        """
        method that creates a new credential
        """
        newCredential = Credentials(
            username, account, password)
        return newCredential

    def searchCredential(account):
        """
        Method that searches for credentials
        """
        if Credentials.credentials:
            for credential in Credentials.credentials:
                if credential.account == account:
                    return credential
            print(" There is no account with those credentials")

        else:
            print("Credentials have not been saved")

    def displayCredential():
        """
        Method that displays saved credentials
        """
        if (len(Credentials.credentials) > 0):

            return Credentials.credentials

    @classmethod
    def credentialExist(self, account):
        """
        Method that checks if credentials exists
        """

        if Credentials.credentials:
            for credential in Credentials.credentials:
                if credential.account == account:
                    return True
            print("Account doesn't exist.Create one to proceed")

        else:
            print("Credentials Not saved")

    def deleteCredential(account):
        """
        Method that deletes credential
        """
        for credential in Credentials.credentials:
            if credential.username == account:
                Credentials.credentials.remove(credential)

    def passwordGenerate(stringLength=8):
        """
        Method that generate a random password
        """
        password = string.asxcii_lowercase + string.ascii_uppercase + "~!@#$%;:^&*"
        return ''.join(random.choice(password) for i in range(int(stringLength)));