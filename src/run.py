from lucy import settings
from lucy.utils.startup import internet_connectivity_check
from lucy.core.processor import Processor
from lucy.core.console import ConsoleManager as cm

from lucy.utils import  startup

def main():
    """
    Do initial checks, clear the console and print the assistant logo.
    """

    cm.console_output(info_log='Wait a second for startup checks..')
    internet_connectivity_check()

    cm.console_output(info_log='Application started')
    cm.console_output(info_log="I'm ready! Say something :-)")

    processor = Processor()
    while True:
        processor.run()


if __name__ == '__main__':
    main()