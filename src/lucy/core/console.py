
import subprocess
import os
import psutil
import logging

from lucy.utils.console import bot_logo, start_text, OutputStyler


class ConsoleManager:
    @classmethod
    def clear(cls):
        """
        Clears stdout

        Check and make call for specific operating system
        """

        subprocess.call('tput reset' if os.name == 'posix' else 'cls', shell=True)
    @classmethod
    def console_output(cls, text='', debug_log=None, info_log=None, warn_log=None, error_log=None, refresh_console=True):
        """
        Output example:

              ║██      ╗ ██   ██╗ ███████╗   ██╗    ╗██
              ║██      ║ ██   ██╗ ██╔══╗      ██   ██
              ║██      ║ ██  ║██  ██           ║█  █║
              ║██      ║ ██   ██║ ██╔══╗         ██
              ║██████ ╔╝ ███████║ ███████║       ██
               ╚════╝  ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝
        ---------------------------------------- SYSTEM --------------------------------------------------
        RAM USAGE: 0.14 GB
        ----------------------------------------- LOG ----------------------------------------------------
        2020-04-25 19:22:51,524 - root - INFO - Startup checks..
        2020-04-25 19:22:51,534 - root - DEBUG - Internet connection check..
        2020-04-25 19:22:51,773 - root - INFO - Internet connection passed!
        2020-04-25 19:22:51,783 - root - INFO - Application started

        ---------------------------------------- ASSISTANT ------------------------------------------------
        > The current date is: 2020-04-25
        -------------------------------------------- - ----------------------------------------------------
        """

        if refresh_console:
            cls.clear()

            # ----------------------------------------------------------------------------------------------------------
            # Logo sector
            # ----------------------------------------------------------------------------------------------------------
            cls._stdout_print(bot_logo + start_text)
            print(OutputStyler.BOLD +
                  'RAM USAGE: {0:.2f} GB'.format(cls._get_memory()) + OutputStyler.ENDC)

            # ----------------------------------------------------------------------------------------------------------
            # Assistant logs sector
            # ----------------------------------------------------------------------------------------------------------

            if debug_log:
                logging.debug(debug_log)

            if info_log:
                logging.info(info_log)

            if warn_log:
                logging.warning(warn_log)

            if error_log:
                logging.error(error_log)


            if text:
                print(OutputStyler.BOLD + '> ' + text + '\r' + OutputStyler.ENDC)

        else:
            if text:
                print(OutputStyler.BOLD + text + '\r' + OutputStyler.ENDC)

    @staticmethod
    def _get_memory():
        """
        Get assistant process Memory usage in GB
        """
        pid = os.getpid()
        py = psutil.Process(pid)
        return py.memory_info()[0] / 2. ** 30

    @staticmethod
    def _stdout_print(text):
        """
        Application stdout with format.
        :param text: string
        """
        print(OutputStyler.CYAN + text + OutputStyler.ENDC)
