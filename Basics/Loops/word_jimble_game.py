import random
import sys

# create a list to chose from it
while True:

    word_list = ["computer", "games", "football", "ocean", "mobile", "desktop"]

    # choose a word from the list
    word = random.choice(word_list)

    # jumble the letter of the word and display it
    shuffled_word = "".join(random.sample(word, len(word)))
    print(f"Jumbled word: {shuffled_word}")

    score = 0

    while True:
        # prompt the user to enter his guess
        guessed_word = input("Enter your guess: ")

        if guessed_word == word:
            print("Congrats, the word is correct")
            break
        else:
            print("Sorry, the word is not correct, try again")
            score -= 1
            break

    print(f"Score: {score}")
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        sys.exit("Thanks for playing")
