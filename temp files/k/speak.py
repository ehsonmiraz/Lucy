import pyttsx3
from lucy.skills.settings import *

class TTS:
    """
    Text To Speech Engine (TTS)
    """

    def __init__(self):
        self.engine = self._set_voice_engine()

    def run_engine(self):
        try:
            self.engine.runAndWait()
        except RuntimeError:
            print("error in runwait")
            pass

    @staticmethod
    def _set_voice_engine():
        """
        Setup text to speech engine
        :return: gtts engine object
        """
        tts_engine = pyttsx3.init()
        tts_engine.setProperty('rate', RATE)  # Setting up new voice rate
        tts_engine.setProperty('volume', VOL)  # Setting up volume level  between 0 and 1
        tts_engine.setProperty('voice', VOICE)
        return tts_engine

class Speak(TTS):

    def __init__(self):
        super().__init__()
        print(self.engine)
        #voi = self.engine.getProperty('voices')
        self.engine.setProperty('rate', RATE)
        self.engine.setProperty('voice', VOICE)
        self.engine.setProperty('volume', VOL)

    def say1(text):
          print(text)

    def say2(self,text,vol=VOL,rate=RATE):
        batches=["hello babu","how are you", "kill it"]
        if(vol!=VOL or rate!=RATE):
            self.engine.setProperty('rate', rate)
            self.engine.setProperty('voice', 'english')
            self.engine.setProperty('volume', vol)
        for batch in batches:
            self.engine.say(batch)
            self.engine.runAndWait()

    def say3(text):
         import os
         file=open('/home/pi/Desktop/jarvis2/text.txt' ,'w')
         file.write(text)
         file.close()
         os.system('bash /home/pi/Desktop/jarvis2/pico.bash')
         print("done")

    say = say2
if __name__=='__main__':
     Speak().say("hey have you watched , avenger infinity wars . You should see it , its a nice movie")#"either, you, die, a ,hero. or. live long and watch yourself becoming a villain -joker")




#CRCJL8Q9
