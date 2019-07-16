# Create your Game class logic in here.
import re
import os
from phrasehunter.phrase import Phrase


class Game():
    """The class should include an initializer or def __init__ method that receives a phrases parameter
    and holds these phrases in an instance attribute on the game object.
    You will likely need at least 1 instance attribute:
    An instance attribute that stores the current Phrase object for the start of the game.
    You may think of this as the Active phrase being guessed against by the player while the game is running.
    The Game instance might be responsible for things like: starting the game loop,
    getting player's input() guesses to pass to a Phrase object to perform its responsibilities against,
    determining if a win/loss happens after the player runs out of turns or the phrase is completely guessed."""

    def __init__(self, *phrases):
        self.guess = False
        self.life = 5
        self.Activephrase = []
        for phrase in phrases:
            self.Activephrase.append(Phrase(phrase))


    def get_letter(self):
        """ get the letter from player and only can except chatacter.
        if not a character, need to get again"""
        while True:
            try:
                letter = input("Guess a letter:")
            except KeyboardInterrupt:
                action = input("\ndo you really want to exit? Y/N >")
                if action.upper() == "Y":
                    os._exit(0)
            # check only one letter
            if len(letter) > 1 :
                print("the length of letter is not 1!!")
                continue
            # check it's not number or others, only english character
            elif re.match(r"\w", letter) == None:
                print("it's no an character!!")
                continue
            else:
                return letter


    def check_the_guess(self,phrase,letter):
        """ checking that whether get a new character or not """
        self.guess = phrase.letter_in_pharase(letter)



    def win_or_not(self,phrase):
        """ all characters are guessed or not, if all guessed and the player win and display the answer"""
        if phrase.whether_all_gaused():
            phrase.show_the_pharse()
            print("\n\tYou win!! ")
            return True
        else:
            # still not win the game
            return False

    def _play_again(self):
        """ask whether play again on the same pharse"""
        try:
            play_again = input("\ndo you wan to play again? Y/N >")
        except KeyboardInterrupt:
            action = input("\ndo you really want to exit? Y/N >")
            if action.upper() == "Y":
                os._exit(0)
        if play_again.upper() == "Y":
            return True
        else:
            return False


    def _play_next(self):
        """ask whether play the next phrase"""
        try:
            play_again = input("\ndo you wan to play next game? Y/N >")
        except KeyboardInterrupt:
            action = input("\ndo you really want to exit? Y/N >")
            if action.upper() == "Y":
                os._exit(0)
        if play_again.upper() == "Y":
            return True
        else:
            return False


    def check_life(self,answer):
        if answer == False:
            self.life -= 1
            print("wrong, now Your life is {}!!".format(self.life))
        if self.life == 0:
            print("\n\tGame over!")
            return self.life
        else:
            return True

    def reset_game(self,hidden_phrase):
        self.guess = False
        self.life = 5
        hidden_phrase.reset_phrase()



    def game_on(self):
        print("staring game:")
        for hidden_phrase in self.Activephrase:
            while True:
                hidden_phrase.show_the_pharse()
                # getting the letter and check whether the player's guess is right
                self.check_the_guess(hidden_phrase, self.get_letter())
                # life status,  if life is 0 then the player loss
                if self.check_life(self.guess) == 0:
                    if self._play_again():
                        self.reset_game(hidden_phrase)
                    else:
                        print("exit game!!\n")
                        os._exit(0)

                if self.win_or_not(hidden_phrase):
                    if self._play_next():
                        break
                    else:
                        print("exit game!!\n")
                        os._exit(0)
            print("no more Guess, Game finished")


    def show_all_the_phrase(self):
        for phrase in self.Activephrase:
            print(type(phrase))
            for char in phrase:
                # why this char class is not Character but str?
                print(type(char))
                print(char)
