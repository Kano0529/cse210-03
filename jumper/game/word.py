
import random

class Word:
    """The word that a player supposed to guess.

    The responsibility of Word is to keep track of the word being guessed.

    Attributes:
        _word_list(list): list of the target word to choose from
        _target_word(string): the word in the _word_list that a player supposed to guess
        _letter_list(list): list of letters that are in the _target_word
        _current_word(string): the word that is manipulated with each guess
        _current_list(list): the list version of the _target_word
        _guessed_list(list): list of the letters that are guessed correctly
    """

    def __init__(self):
        """Constructs a new Word.

        Args:
            self(Word): An instance of Word
        """

        self._word_list = ["information", "confusion", "accerelation" ]
        self._letter_list = []
        self._current_word = ''
        self._current_list = []
        self._guessed_list = []
   
        self._target_word = random.choice(self._word_list)  # a target word is chosen
        self._letter_list = list(self._target_word)   # make a list of letters that are in the target word



    def get_initial_word(self):
        """Sets an initial value, which is '_', of the _current_word and a list version
        of the _current_word.

        Args:
            self(Word): an instance of Word

        return:
            initial set of word with '_'    
        """
    
        for i in range(len(self._target_word)):   # _current_word is padded with '_'
            self._current_word += '_'             # for the length of the target word

        self._current_list = list(self._current_word)   # list version of the _current_word

        return self._current_word 



    def wrong_guess(self, guessed):
        """Gets a player's guess and finds out if it is the correct guess.

        Args:
            self(Word): an instance of Word
            guessed(string): a letter a player guessed

        return:
            boolean: True if a player guessed wrong    
        """

        if guessed in self._letter_list:         # if a player guessed right
            self._guessed_list.append(guessed)   # appends it to the guessed_list
            return False                         # sets wrong_guess to be false
        else:
            return True                          # otherwise wrong_guess is true   


    def set_word(self):
        """Substitutes _current_word with the letter guessed.
        
        Args:
            self(Word): an instance of Word

        Return:
            _current_word padded with the right guessed letter.    
        """
           
        for i in range(len(self._current_list)):             # if list version of target word is in the 
            if self._letter_list[i] in self._guessed_list:   # right guessed letter list,
                self._current_list[i] = self._letter_list[i] # swap a list version of current word with 
                                                             # the letter
        self._current_word = "".join(self._current_list)     # _current_word gets _current_list(list is now a string)

        return self._current_word 


    def  complete_word(self):
        """Checks if a word is completed with letters.
        Args:
            self(Word): an instance of Word
        return:
            True if all '_' is substituted with letters in a _current_list    
        """
        if '_' in self._current_list:
            return False
        else:
            return True                             
