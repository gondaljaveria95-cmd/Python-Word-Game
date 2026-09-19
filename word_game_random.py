import random

words = ["apple", "grape", "house", "plant", "chair"]

secret_word = random.choice(words)

attempt = 0

while attempt < 6:
    guess = input("Guess the word: ").lower()

    if len(guess) != len(secret_word):
        print("Please enter a 5 letter word.")
        continue

    if guess == secret_word:
        print("This is your answer!")
        break
    else:
        print("Your guess is wrong!")

    for index, letter in enumerate(guess):
        if letter == secret_word[index]:
            print(letter, "Correct Position")
        elif letter in secret_word:
            print(letter, "Wrong Position")
        else:
            print(letter, "is not present")

    attempt = attempt + 1
    print("Attempts Left:", 6 - attempt)

    if attempt == 6:
        print("Game Over!")
        print("The correct word was:", secret_word)