2.Simple Login System

# Pre-defined username and password

_username = "admin"
_password = "12345"

# Accept input from the user
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check username first
if username == _username:
    # If username is correct, check password
    if password == _password:
        print("Login successful! ✅")
    else:
        print("Incorrect password. ❌")
else:
    print("Incorrect username. ❌")

#Output
Enter your username: drishtipandey
Enter your password: 12345
Incorrect username. ❌    
