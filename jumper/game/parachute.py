class Parachute:
    """A parachute and man drawing for the game. 
    The responsibility of Parachute is to handle the parachute and man drawing when a player
    guesses a letter wrong.

    Attributes:
        _para1(string): parachute line #1
        _para2(string): parachute line #2
        _para3(string): parachute line #3
        _para4(string): parachute line #4
        _parachute(string): concatenated version of a whole parachute
        _man1(string): man line #1
        _man2(string): man line #2
        _man3(string): man line #3
        _man4(string): man line #4
        _man(string): concatenated version of a man
        _lastman(string): x face of a man
        _size(integer): size of a parachute 
    """
    def __init__(self):
        """Sets the initial value for parachute and man.

        Args:
            self(Parachute): an instance of Parachute
        """
        
        self._para1 = '  ___'
        self._para2 = " /___\\"
        self._para3 = " \\   /"
        self._para4 = "  \\ /"
        self._parachute = f"{self._para1}\n{self._para2}\n{self._para3}\n{self._para4}"
    

        self._man1 = "   o"
        self._man2 = "  /|\ "
        self._man3 = "  / \ "
        self._man4 = ' '
        self._man5 = "^^^^^^^"
        self._man = f"{self._man1}\n{self._man2}\n{self._man3}\n{self._man4}\n{self._man5}"
        self._lastman = "   x"

        self._size = 4
        

    def get_size(self):
        """Decrement the size of parachute

        Arg: self(Parachute): an instance of Parachute
        """   
        self._size = self._size - 1   


    def set_parachute(self):
        """Construct a new Parachute.

        Args: 
            self(Parachute): an instance of Parachute

        Returns:
            a parachute with correct number of lines    
        """
        if self._size == 4:
            self._parachute = f"{self._para1}\n{self._para2}\n{self._para3}\n{self._para4}"
        elif self._size == 3:
            self._parachute = f"{self._para2}\n{self._para3}\n{self._para4}" 
        elif self._size == 2:
            self._parachute = f"{self._para3}\n{self._para4}" 
        elif self._size == 1:
            self._parachute = f"{self._para4}" 
        elif self._size == 0:
            self._parachute = ''

        return self._parachute 


    def set_man(self):
        """Sets a string for man according to the size.

        Args:
            self(Parachute): an instance of Parachute

        Returns:
            a man with face 'o' or 'x'    
        """
        if self._size == 0:
            self._man = f"{self._lastman}\n{self._man2}\n{self._man3}\n{self._man4}\n{self._man5}" 
        else:
            self._man = f"{self._man1}\n{self._man2}\n{self._man3}\n{self._man4}\n{self._man5}"

        return self._man  


    def has_parachute(self):
        """Checks if a parachute is empty.

        Args:
            self(Parachute): an instance of Parachute

        Returns:
            True if there are more parachute that could be drawn.    
        """
        if self._parachute != '':
            return True       
