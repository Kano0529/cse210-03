
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

        if guessed in self._letter_list:         #
            self._guessed_list.append(guessed)
            return False
        else:
            return True    


    def set_word(self):
           
        for i in range(len(self._current_list)):
            if self._letter_list[i] in self._guessed_list:
                self._current_list[i] = self._letter_list[i]  

        self._current_word = "".join(self._current_list)

        return self._current_word 


    def  complete_word(self):
        if '_' in self._current_list:
            return False
        else:
            return True                             
