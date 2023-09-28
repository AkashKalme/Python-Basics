# Exercise: Password Checker
username = input("Enter Username: ")
password = input("Enter Password: ")

password_length = len(password)
hidden_password = '*'*password_length

print(f"{username}, your password {hidden_password} is {password_length} letters long.")
