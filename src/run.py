from lucy import settings
from lucy.utils.startup import internet_connectivity_check
from lucy.core.processor import Processor
from lucy.core.console import ConsoleManager


def main():
    """
    Do initial checks, clear the console and print the assistant logo.
    """
    console_manager = ConsoleManager()
    console_manager.console_output(info_log='Wait a second for startup checks..')
    internet_connectivity_check()
    console_manager.console_output(info_log='Application started')
    console_manager.console_output(info_log="I'm ready! Say something :-)")
    processor = Processor(console_manager=console_manager, settings_=settings)

    while True:
        processor.run()


if __name__ == '__main__':
    main()