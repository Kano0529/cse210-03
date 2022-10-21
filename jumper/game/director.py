from game.parachute import Parachute
from game.word import Word
from game.terminal_service import TerminalService


class Director:
    """A person who directs the game.
    The responsibility of a Director is to control the sequence of a game.

    Attributes:
        _parachute(Parachute): The game's parachute.
        _word(Word): The game's word
        _terminal_service: for getting and displaying information
        _current_word(string): a word with current value
        _current_parachute(string): a parachute with current value
        _current_man(string): a man with current value
        _your_guess(string): input letter
        _missed(boolean): True if a player guessed wrong
    """
    
    def __init__(self):
        """Constructs a new Director

        Args:
            self(Director): an instance of Director.
        """
        self._parachute = Parachute()
        self._word = Word()
        self._terminal_service = TerminalService()

        self._current_word = ''
        self._current_parachute = ''
        self._current_man = ''
        self._your_guess = ''
        self.missed = False


    def start_game(self):
        """Draws the initial stage of the game and start the game by
        running the main game loop.

        Args:
            self(Director): an instance of Director
        """
        self._current_word = self._word.get_initial_word()
        self._terminal_service.write_text(self._current_word)
        self._current_parachute = self._parachute.set_parachute()
        self._terminal_service.write_text(self._current_parachute)
        self._current_man = self._parachute.set_man()
        self._terminal_service.write_text(self._current_man)

        while not self._word.complete_word() and self._parachute.has_parachute():
            self._get_input()
            self._do_update()
            self._do_output()

        if self._parachute.has_parachute():
            self._terminal_service.write_text("You did it!")
        else:
            self._terminal_service.write_text("try again!")        


    def _get_input(self):
        """Get a letter as an input and checks if it is a right guess.

        Args:
            self(Director): an instance of Director
        """
        self._your_guess = self._terminal_service.read_text("Guess a word [a-z]? ")
        self.missed = self._word.wrong_guess(self._your_guess)


    def _do_update(self):
        """Sets a value for new parachute if a player guessed wrong or for a new 
        current word if guessed right.

        Args:
            self(Director): an instance of Director
        """
        if self.missed:
            self._parachute.get_size()
            self._current_parachute = self._parachute.set_parachute()
            self._current_man = self._parachute.set_man()
        else:
            self._current_word = self._word.set_word()
 


    def _do_output(self):
        """Provides outputs to terminal_service

        Args:
            self(Director): an instance of Director
        """
        self._terminal_service.write_text(self._current_word)
        self._terminal_service.write_text('')
        self._terminal_service.write_text(self._current_parachute)
        self._current_man = self._parachute.set_man()
        self._terminal_service.write_text(self._current_man) 

               



