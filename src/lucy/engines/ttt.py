import logging
from lucy.core.console import ConsoleManager
from lucy.utils.console import user_input


class TTTEngine:
    """
    Text To Text Engine (TTT)
    """
    def __init__(self):
        self.logger = logging
        self.console_manager = ConsoleManager()

    def recognize_input(self, **kwargs):
        """
        Recognize input from console and returns transcript if its not empty string.
        """
        try:
            text_transcript = input(user_input).lower()
            while text_transcript == '':
                text_transcript = input(user_input).lower()
            return text_transcript
        except EOFError as e:
            self.console_manager.console_output(error_log='Failed to recognize user input with message: {0}'.format(e))

    def respond(self, message, refresh_console=True):
        """
        Assistant response in voice or/and in text.
        :param refresh_console: boolean
        :param message: string
        """
        try:
            if message:
                self.console_manager.console_output(message, refresh_console=refresh_console)
        except RuntimeError as e:
            self.console_manager.console_output(error_log='Error in assistant response with message: {0}'.format(e))
