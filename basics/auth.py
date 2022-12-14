class User : 
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def CheckUser(self, username, password):
        if username == self.username and password == self.password :
            print("Logged in successfully!") 
            return True
        else :
            print("Authentication failed!")
            return False

while True: 
    print("Create your account!")
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = User(username, password)
    print(f"User {user.username} created successfully")
    print("Log in User")
    username2 = input("Enter username: ")
    password2 = input("Enter password: ")  
    user.CheckUser(username2, password2)
    break;
