correctUsername = "vtalla"
correctPassword = "vishal@1234"

maxAttempts = 0

while maxAttempts <= 3:
    inputUserName = input("enter user name: ")
    inputPassword= input("enter Password: ")

    if correctUsername == inputUserName and correctPassword == inputPassword:
        print("Login GOOD")
    else:
        maxAttempts += 1
        print("Login FAILED")
       
print("Max attempts reached Account Blocked")
