import random


class Word:
    """The word that the player needs to guess.

    The responsibility of Word is to check if the player is guessing the word correctly.

    Attributes:
        _word_list (list): A list of random words.
        _current_word (str): A random word chosen from a list.
        _hidden_word (list): An empty list to be filled with underscores.
    """

    def __init__(self):
        """Constructs a new Word.

        Args:
            self (Word): An instance of Word
        """
        self._word_list = [
            'information', 'confusion', 'accerelation', 'redeem', 'generator', 'bandit', 'cellphone',
            'hotdog', 'juxtaposition', 'ostrich', 'absolute', 'weakness', 'criminal', 'rhetoric'
            ]
        self._current_word = random.choice(self._word_list)
        self._hidden_word = []

        for _ in range(len(self._current_word)):
            self._hidden_word.append('_')

    def get_hidden_word(self):
        """Gets the current chosen word.

        Args:
            self (Word): An instance of Word

        Returns:
            _hidden_word (list): An empty list filled with underscores.
        """
        return ' '.join(self._hidden_word)

    def set_hidden_word(self, letter):
        """Substitutes an underscore in the hidden word with the letter guessed
        if the letter is in the word.
        
        Args:
            self (Word): An instance of Word
        """
        for i in range(len(self._current_word)):
            if letter == self._current_word[i]:
                self._hidden_word[i] = self._current_word[i]

    def check_guess(self, guess):
        """Checks if the guessed letter is in the word.
        
        Args:
            self (Word): An instance of Word

        Returns:
            boolean: True to delete a line in the parachute.
        """
        if guess in self._current_word:
            return False
        else:
            return True

    def check_hidden_word(self):
        """Check if the hidden word has any underscore in it.

        Returns:
            boolean: True if there are underscores.
        """
        if '_' in self._hidden_word:
            return True
        else:
            return False