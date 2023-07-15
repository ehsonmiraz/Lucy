
import lucy
import os
import time
from datetime import datetime

from lucy.utils.startup import play_activation_sound
from lucy.core.console import  ConsoleManager as cm

class ActivationSkills:

    @classmethod
    def assistant_power_off(cls,_):
        """
        - Clear console
        - Shutdown the assistant service
        """
        lucy.output_engine.respond('Bye')
        time.sleep(1)
        cm.console(info_log='Application terminated gracefully.')
        os.system('shutdown')

    @classmethod
    def assistant_greeting(cls,_):
        """
        Assistant greeting based on day hour.
        """
        now = datetime.now()
        day_time = int(now.strftime('%H'))

        if day_time < 12:
            lucy.output_engine.respond('Good morning sir')
        elif 12 <= day_time < 18:
            lucy.output_engine.respond('Good afternoon sir')
        else:
            lucy.output_engine.respond('Good evening sir')
