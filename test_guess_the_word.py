# Hunter Francis
# CIS256 Fall 2025
# EX 4
# Test file

import pytest
import random
from guess_the_word import WordGuesser

words = ["syntax", "argument", "class", "array", "iteration", "algorithm"]
game = WordGuesser(words)

# Function used to test that the random word is from the predetermined list
def test_word_from_list():
    secret_word = random.choice(words).lower()
    assert secret_word in words

# Function used to test that guesses follow the set rules.  
def test_process_guess():
    assert game.process_guess('a') == True
    assert game.process_guess('al') == False
    assert game.process_guess('$') == False


