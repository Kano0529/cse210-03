from game.parachute import Parachute
from game.word import Word
from game.terminal_service import TerminalService


class Director:
    
    def __init__(self):
        self._parachute = Parachute()
        self._word = Word()
        self._terminal_service = TerminalService()

        self._current_word = ''

        self._current_parachute = ''
        self._current_man = ''
        self._your_guess = ''
        #
        # self._word_completed = False
        self.missed = False


    def start_game(self):
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

        if self._parachute.has_parachute:
            self._terminal_service.write_text("Try again!")
        else:
            self._terminal_service.write_text("You did it!")        


    def _get_input(self):
        self._your_guess = self._terminal_service.read_text("Guess a word [a-z]? ")
        self.missed = self._word.wrong_guess(self._your_guess)


    def _do_update(self):
        if self.missed:
            self._parachute.get_size()
            self._current_parachute = self._parachute.set_parachute()
            self._current_man = self._parachute.set_man()
        else:
            self._current_word = self._word.set_word()
 


    def _do_output(self):
        self._terminal_service.write_text(self._current_word)
        print()
        self._terminal_service.write_text(self._current_parachute)
        self._current_man = self._parachute.set_man()
        self._terminal_service.write_text(self._current_man) 

               




