import random

# List of words
words = ["python", "github", "hangman", "computer", "programming"]

# Select random word
word = random.choice(words)

# Create empty display
guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman Game!")

# Game loop
while attempts > 0:
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if player won
    if "_" not in display:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        print("Good guess!")
        guessed_letters.append(guess)
    else:
        print("Wrong guess!")
        attempts -= 1
        print("Attempts left:", attempts)

if attempts == 0:
    print("💀 Game Over! The word was:", word)
