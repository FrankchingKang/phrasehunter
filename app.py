# Import your Game class

# Create your Dunder Main statement.

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop

from phrasehunter.character import Character
from phrasehunter.phrase import Phrase
from phrasehunter.game import Game


if __name__ == "__main__":

    Guess_words = Game("apple","book","logitech","dell","amuze")
    Guess_words.game_on()

    #Guess_words.show_all_the_phrase()
