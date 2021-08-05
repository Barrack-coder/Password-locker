# import unittest
# from user import user
# from user import credentials

# class TestClass(unittest.TestCase):
        
#         def setUp(self):
# 	    #method used to run the test
# 	           self.new_user("Barry","Barry@123")
#         def test_init(self):
#                 self.assertEqual = (self.new_user.userName, "Barry")
#                 self.assertEqual = (self.new_userPassword,"Barry@1234")
#         def test_save_user(self):
#                 self.new_user.save_user()
#                 self.assertEqual (len(user.user_list),1)

	

from run import Credentials, User


if __name__ == "__main__":
    
    isTrue = True
    print("What is your name?")
    name= input()
    print(f"Hello {name} Welcome to password manager.An application that manages and generate passwords for you.")
    while isTrue == True:
        print(
            "Use these short codes to proceed:\n\n 1. ca-Create new Account\n 2. ha-Have an existing Account\n")
        shortCode = input().lower()

        if shortCode == 'ca':
            print("Create New Account")
            print("*"*50)
            print("Username")
            username = input()

            while True:
                print(
                    "1. tyop - Type your own password\n 2. gp - generate password from system")
                password = input()

                if password == 'tyop':
                    print("Enter your Password:")
                    password = input()
                    break
                elif password == 'gp':
                    password = Credentials.passwordGenerate()
                    break

                else:
                    print("password is Incorrect")

            createUser = User.createUser(username, password)
            User.saveUser(createUser)
            print("\n")
            print(
                f"Hi {username} Your account has been created sucessfully !\n")
            print(f"Your username is: {username} \n Your password is: {password}\n")

        elif shortCode == 'ha':
            print("*"*100)
            print("Enter your username and password ASAP!")
            print("*"*100)

            print("Enter Username:")
            username = input()
            print("Enter Password:")
            password = input()

            for user in User.userList:
                if username == user.username:
                    if user.password == password:
                        print(user.login())
                    else:
                        print("password enterd is incorrect")
                        break
                else:
                    print("username enetered is  Incorrect")
                    break

            break
    while True:
        print("If you would like to proceed use the shortcodes below\n 1. sc - Save Credential \n 2. dc - Display Existing Credential\n 3. fc - Find credential \n 4. del -  Delete an existing Credential \n 5. ex - Exit")

        shortCode = input().lower()

        if shortCode == 'sc':
            print("Enter Your New Credential Account:")
            print("*"*100)
            print("\n")

            print("Enter Account Name e.g email:")
            account = input()

            print("Enter Account UserName:")
            username = input()

            while True:
                print(
                    "1. tp - type your own password?\n 2. gp -generate password from system")

                password = input().lower()

                if password == 'tyop':
                    print("Type Account Password :")
                    password = input()
                    break
                elif password == 'gp':
                    password = Credentials.passwordGenerate()
                    break

                else:
                    print("Password Entered is Incorrect")

            newCredential = Credentials.createCredential(
                account, username, password)
            Credentials.saveCredential(newCredential)
            print("\n")
            print("Your Account Credentials has been saved!")
            print("\n")

        elif shortCode == 'dc':
            if Credentials.displayCredential():
                print(" Here is a List of your credentials:\n")
                for credential in Credentials.credentials:
                    accountuser = credential.username    
                    account = credential.account
                    accountpassword = credential.password
                    print(
                        f"Account Name : {account}\n Account Username : {accountuser}\n Account Password: {accountpassword}\n")

            else:
                print("You do not have any saved credentials\n")

        elif shortCode == 'fc':
            print("Enter Account name: ")
            Account = input()
            if Credentials.credentialExist(Account):
                searchAccount = Credentials.searchCredential(Account)
                print(
                    f"Account name: {searchAccount.account}\n Account Username: {searchAccount.username}\n Account Password : {searchAccount.password}")

            else:
                print("account name doesn't exist!\n")

        elif shortCode == 'del':
            print("Enter credential that you would like to be deleted")
            Account = input()
            if Credentials.credentialExist(Account):
                Credentials.deleteCredential(Account)
                print("Account has been Successfully deleted")

            else:
                print("account name doesn't exist here")

        elif shortCode == 'ex':
            print("Thank you for using this application.")
            break

        else:
            print("incorrect code")  
     
