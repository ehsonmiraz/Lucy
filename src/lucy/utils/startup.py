import os
import time
import requests
import logging
from playsound import playsound
from lucy.utils import console
from lucy.core.console import ConsoleManager


def play_activation_sound():
    """
    Plays a sound when the assistant enables.
    """
    utils_dir = os.path.dirname(__file__)
    activation_soundfile = os.path.join(utils_dir, '..', 'files', 'activation_sound.wav')
    playsound(activation_soundfile)


def internet_connectivity_check(url='http://www.google.com/', timeout=2):
    """
    Checks for internet connection availability based on google page.
    """
    console_manager = ConsoleManager()
    try:
        console_manager.console_output(info_log='Checking internet connection..')
        _ = requests.get(url, timeout=timeout)
        console_manager.console_output(info_log='Internet connection passed!')
        return True
    except requests.ConnectionError:
        console_manager.console_output(warn_log="No internet connection.")
        console_manager.console_output(warn_log="Skills with internet connection will not work")
        return False
