from random import choice

def hangman_game():

    print("\n\n-------------------------------------")
    print("|            Hangman Game           |")
    print("-------------------------------------")

    while True:

        words = ["python", "hangman", "programming", "challenge", "developer", "computer", "software", "algorithm", 
                "keyboard", "function", "variable", "debugging", "recursion", "loop", "syntax", "interface", 
                    "framework", "database", "network", "artificial"]
        word = choice(words)

        attempts = len(word) + 5
        guessed_letters = []

        print("\nWord Length: " , len(word))

        while attempts != 0:

            guessed_letter = input("\nEnter a new guessed letter: ").lower()

            if guessed_letter not in word:
                print("\nLetter does not exist in the word.")

            else:
                guessed_letters.append(guessed_letter)

            display = ""
            for letter in word:
                if letter in guessed_letters:
                    display += letter
                else:
                    display += "_"

            print("\nCurrent Word: " + display)
            print("Guessed Letters: " + ', '.join(guessed_letters))

            if set(guessed_letters) >= set(word):
                print("\nCongratulations! You guessed the word correctly: " + word)
                break

            attempts -= 1
            print("\nAttempts Left: " , attempts)
            
        print("\nThe word was: " + word)

        another_game = input("\nDo you want to play another game? (y/n): ")

        if another_game.lower() != "y":
            break

hangman_game()
