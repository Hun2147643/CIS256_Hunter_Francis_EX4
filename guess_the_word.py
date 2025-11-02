# Hunter Francis
# CIS256 Fall 2025
# EX 4

import random


class WordGuesser:
    # Initializes the WordGuesser game.
    def __init__(self, word_list, max_attempts=7):
        # Randomly selects a word from the words list and sets it equal to secret_word.
        self.secret_word = random.choice(word_list).upper()
        # Creates an empty set to hold the guessed letters.
        self.guessed_letters = set()
        # Sets the max number of attempts the user has to guess the word correctly.
        self.attempts_left = max_attempts
        # Used to display underscores while user attempts to guess word.
        self.display_word = ["_" for _ in self.secret_word]

    def display_current_state(self):
        
        # Prints the current state of the game, including the word and attempts left.
        print("\nWord: " + " ".join(self.display_word))
        print(f"Attempts left: {self.attempts_left}")
        print(f"Guessed letters: {', '.join(sorted(list(self.guessed_letters)))}")

    def process_guess(self, guess):

        guess = guess.upper()

        # Adds guessed letters to guessed_letters set
        self.guessed_letters.add(guess)

        # Checks whether user's guess is in the secret_word and informs user of appropriate response.
        if guess in self.secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(self.secret_word):
                if letter == guess:
                    self.display_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            self.attempts_left -= 1
        return True

    def check_game_over(self):

        # Checks whether user has won the game by spelling the word or lost by running out of lives.
        if "_" not in self.display_word:
            return "win"
        elif self.attempts_left <= 0:
            return "lose"
        return None

    def play_game(self):
       
        # Runs the main game loop.
        print("Welcome to the Word Guessing game!")
        print(f"The word has {len(self.secret_word)} letters.")
        while True:
            self.display_current_state()
            guess = input("Guess a letter: ")
            if self.process_guess(guess):
                game_status = self.check_game_over()
                if game_status == "win":
                    print(f"\nCongratulations! You guessed the word: {self.secret_word}")
                    break
                elif game_status == "lose":
                    print(f"\nGame over! You ran out of attempts. The word was: {self.secret_word}")
                    break

if __name__ == "__main__":
    words = ["syntax", "argument", "class", "array", "iteration", "algorithm"]
    game = WordGuesser(words)
    game.play_game()
