users_account = {"HasanSadaqa": "123456789", "Sajed Sadaqa": "321654987"}
user_name = input("User name: ")
password = input("Password: ")
if user_name in users_account and users_account[user_name] == password:
    print(f"welcome {user_name}!")
else:
    print("Invalid user name or password")
    user_name = input("User name: ")
    password = input("Password: ")
    while user_name not in users_account or users_account[user_name] != password:
        print("Invalid user name or password")
        user_name = input("User name: ")
        password = input("Password: ")
    else:
        print(f"welcome {user_name}!")






