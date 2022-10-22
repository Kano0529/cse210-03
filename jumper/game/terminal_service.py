class TerminalService:
    """A service that handles terminal operation.

    The responsibility of a TerminalService is to provide input and output
    operation for the terminal.
    """

    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def write_text(self, text):
        """Displays the given text in the terminal.

        Args:
            self (TerminalService): an instance of TerminalService.
            text (string): The text to display.
        """
        print(text)

    def write_list(self, given_list):
        """Displays the given list in the terminal.

        Args:
            self (TerminalService): an instance of TerminalService.
            given_list (string): The text to display.
        """
        for i in given_list:
            print(i)