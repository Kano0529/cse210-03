from game.parachute import Parachute
from game.terminal_service import TerminalService
from game.word import Word


class Director:
    """A person who directs the game.

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _parachute (Parachute): The parachute worn by the player.
        _terminal_service (TerminalService): For getting and displaying information on the terminal.
        _word (Word): The game's chosen word.
        _is_playing (boolean): Whether or not to keep playing.
    """
    
    def __init__(self):
        """Constructs a new Director.

        Args:
            self(Director): an instance of Director.
        """
        self._parachute = Parachute()
        self._terminal_service = TerminalService()
        self._word = Word()
        self._is_playing = True
        self._guess = ''

    def start_game(self):
        """Draws the initial stage of the game and starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        # Display the parachute and the hidden word.
        print()
        self._terminal_service.write_text(self._word.get_hidden_word())
        print()
        self._terminal_service.write_list(self._parachute.get_parachute())

        # Start the game loop.
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Asks the user to guess a letter.

        Args:
            self (Director): an instance of Director.
        """
        # Ask the user for a letter and change the underscores in the hidden word.
        self._guess = self._terminal_service.read_text("Guess a letter [a-z]: ")
        self._word.set_hidden_word(self._guess)

    def _do_updates(self):
        """Changes the parachute depending of the guess.

        Args:
            self (Director): an instance of Director.
        """
        # Erase a line of the parachute if the guess was wrong.
        self._parachute.set_parachute(self._word.check_guess(self._guess))
 
    def _do_outputs(self):
        """Provides the outputs to Terminal Service.

        Args:
            self (Director): an instance of Director
        """
        # Display the parachute and the hidden word.
        print()
        self._terminal_service.write_text(self._word.get_hidden_word())
        print()
        self._terminal_service.write_list(self._parachute.get_parachute())

        # If the the parachute is completely erased, the player loses.
        if len(self._parachute.get_parachute()) < 6:
            self._is_playing = False
            print("\nTry again!\n")

        # If the hidden word is uncovered completely, the player wins.
        if not self._word.check_hidden_word():
            self._is_playing = False
            print("\nYou did it!\n")