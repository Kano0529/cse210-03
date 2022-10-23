class Parachute:
    """The drawing of the parachute and the player.

    The responsibility of Parachute is to handle the parachute and the man drawing and
    change depending of the player's guess.

    Attributes:
        _parachute (list): a list containing the strings to draw the parachute and the player.
    """

    def __init__(self):
        """Constructs a new Parachute.

        Args:
            self (Parachute): an instance of Parachute.
        """
        self._parachute = [
            '  ___', 
            ' /___\\', 
            ' \\   /', 
            '  \\ /', 
            '   o', 
            '  /|\ ', 
            '  / \ ', 
            '', 
            '^^^^^^^']

    def get_parachute(self):
        """Gets the parachute.

        Args:
            self (Parachute): an instance of Parachute.

        Returns:
            _parachute (list): a list containing the strings to draw the parachute and the player.
        """   
        return self._parachute

    def set_parachute(self, pop_line):
        """Changes the parachute depending of the player's guess.

        Args:
            self (Parachute): an instance of Parachute.
            erase_line (boolean): whether to delete a line of the parachute or not.
        """
        if pop_line:
            self._parachute.pop(0)

        if len(self._parachute) < 6:
            self._parachute[0] = '   x'