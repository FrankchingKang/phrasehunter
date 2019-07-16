# Create your Character class logic in here.


class Character(object):
    """The class should include an initializer or def __init__ that receives a char parameter, which should be a single character string."""

    def __init__(self,char):
        """An instance attribute to store the single char string character so the Character object will be able to remember the original character.
        You might call this instance attribute original, but that will be up to you.
        An instance attribute to store a boolean value (True or False) of whether or not this letter has had a guess attempted against it.
        You can initialize this to False inside __init__ as any new Character object will start with a default of False meaning it has not been guessed before.
        You might name this instance attribute was_guessed, but that will also be up to you."""
        if len(char) == 1:
            self.original = char
        else:
            self.original = char[0]

        self.was_guessed = False


    def check_the_answer(self,guess):
        """An instance method that will take a single string character guess as an argument when its called.
        The job of this instance method is to update the instance attribute storing the boolean value,
        if the guess character is an exact match to the instance attribute storing the original char passed in when the Character object was created."""
        if guess == self.original:
            self.was_guessed = True
            return True
        else:
            return False




    def show_the_char(self):
        if self.was_guessed:
            print(self.original, end = " ")
        else:
            print("_", end = " ")


    def reset_character(self):
        self.was_guessed = False
