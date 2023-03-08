import random

# Define the secret word
words = ["apple", "banana", "cherry", "orange", "pear"]
secret_word = random.choice(words)

# Create a dictionary of letter counts in the secret word
letter_counts = {}
for letter in secret_word:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

# Set the initial number of guesses
guesses_left = 5

# Play the game
guessed_word = ["_"] * len(secret_word)
word_guessed = False
while guesses_left > 0 and not word_guessed:
    # Print the current state of the guessed word
    print(" ".join(guessed_word))

    # Get the user's guess
    guess = input("Guess a letter: ")

    # Check if the guess is in the secret word
    if guess in letter_counts:
        # Update the guessed word with the new letter
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess

        # Update the letter counts dictionary
        letter_counts[guess] -= 1
        if letter_counts[guess] == 0:
            del letter_counts[guess]

    # Decrement the number of guesses left
    guesses_left -= 1

    # Check if the word has been guessed
    if "_" not in guessed_word:
        word_guessed = True

# Print the final state of the guessed word
print(" ".join(guessed_word))

# Print the final result
if word_guessed:
    print("You guessed the word!")
else:
    print("Sorry, you ran out of guesses. The word was", secret_word)
