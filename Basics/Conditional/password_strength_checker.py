criteria= {
    "length": 8,
    "uppercase": True,
    "lowercase": True,
    "digits": True,
    "special character": True
}

password = input("please enter a password: ")

strength = 0
if len(password) > criteria["length"]:
    strength += 1
if any(c.isupper() for c in password):
    strength += 1
if any(c.islower for c in password):
    strength += 1
if any(c.isdigit() for c in password):
    strength += 1
if any(c in "!@#$%^&*()-+?_=,<>/;:'\"[]{}\\|`~" for c in password):
    strength += 1
if strength == len(criteria):
    print("STRONG password")
else:
    print("weak password")
    if len(password) < criteria["length"]:
        print(f"password must be at least {criteria['length']}")
    if any(c.isupper() for c in password) != criteria["uppercase"]:
        print("- Must contain uppercase letters")
    if any(c.islower() for c in password) != criteria["lowercase"]:
        print("- Must contain lowercase letters")
    if any(c.isdigit() for c in password) != criteria["digits"]:
        print("- Must contain digits")
    if any(c in "!@#$%^&*()-+?_=,<>/;:'\"[]{}\\|`~" for c in password) != criteria["special character"]:
        print("- Must contain special characters")


# password = input("please enter a password: ")
# if len(password) < 9:
#     print("password must be greater than 9 char")
# elif password.islower():
#     print("password must have at least one uppercase character")
# elif password.isupper():
#     print("password must have at least one lowercase character")
# elif password.isnumeric():
#     print("password must have at least one uppercase char and one lowercase char")
# elif not any(c.isdigit() for c in password):
#     print("password must have at least one number")
# elif not any(c in "!@#$%^&*()-+?_=,<>/;:'\"[]{}\\|`~" for c in password):
#     print("password must have special character")
# else:
#     print("the password is strong")
