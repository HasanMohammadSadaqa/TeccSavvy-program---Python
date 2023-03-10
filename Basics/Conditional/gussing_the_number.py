import random

num = random.randint(0, 100)
print(num)

guessed_number = None
while guessed_number != num:
    guessed_number = int(input("please guess the number: "))
    if guessed_number < num:
        print("too low, try again")
    elif guessed_number > num:
        print("too high, try again")
    else:
        print("congrats, you win!")




