import os
import time
import requests
import logging
from playsound import playsound
#import RPi.GPIO as gpio
from multiprocessing import  Process
from lucy.utils import console
from lucy.core.console import ConsoleManager
from lucy.core.gpio_config import FLASHLIGHT
from lucy.gui import current_face_expression
from lucy.gui.face_ex import FaceExEngine
from lucy.core.console import  ConsoleManager as cm
def turn_on_flash_light():
    # gpio.setmode(gpio.BOARD)
    # gpio.setup(FLASHLIGHT, gpio.OUT)
    return

def play_activation_sound():
    """
    Plays a sound when the assistant enables.
    """
    try:
        utils_dir = os.path.dirname(__file__)
        activation_soundfile = os.path.join(utils_dir, '..', 'files', 'activation_sound.wav')
        #playsound(activation_soundfile)
    except Exception as e:
        cm.console_output(f"unable to play sound : {e}")

def start_face_expression_service():
    p = Process(target=FaceExEngine.run, args=(current_face_expression.face_ex_queue,))
    p.start()
    cm.console_output("face service started")

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


if(__name__=='__main__'):
    start_face_expression_service()