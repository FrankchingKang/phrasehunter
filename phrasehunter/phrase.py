# Create your Phrase class logic here.
from phrasehunter.character import Character

class Phrase(list):
    """The class should include an initializer or def __init__ that receives a phrase
    parameter and holds this phrase in an instance attribute on the Phrase object.
    A phrase should be a collection of Character objects,
    where each letter of the phrase is a Character() instance stored inside a collection such as a List.

The Phrase instance might be responsible for things like: Knowing if the entire phrase has been guessed,
Iterating over its collection of Character to allow a guess to be checked using a Character instance method call or
 to ask the Character object how it should show its letter.

The instance method names and their implementation are up to you to determine.
    """

    def __init__(self, phrases):
        super().__init__(phrases)
        self.phrase = []
        self.guessed = False
        for char in phrases:
            self.phrase.append(Character(char))


    def whether_all_gaused(self):
        for char in self.phrase:
            if char.was_guessed == False:
                return False
        return True


    def show_the_pharse(self):
        print("")
        for char in self.phrase:
            char.show_the_char()
        print("")


    def letter_in_pharase(self, letter):
        self.guessed = False
        for char in self.phrase:
            if char.was_guessed == False and char.check_the_answer(letter):
                self.guessed = True
        return self.guessed


    def reset_phrase(self):
        self.guessed = False
        for char in self.phrase:
            char.reset_character()


"""
Activephrase = Phrase('apple')


Activephrase.show_the_pharse()

print(Activephrase.whether_all_gaused())

Activephrase.letter_in_pharase('a')
Activephrase.show_the_pharse()
print(Activephrase.whether_all_gaused())

Activephrase.letter_in_pharase('l')
Activephrase.show_the_pharse()
print(Activephrase.whether_all_gaused())

Activephrase.letter_in_pharase('p')
Activephrase.show_the_pharse()
print(Activephrase.whether_all_gaused())
"""
