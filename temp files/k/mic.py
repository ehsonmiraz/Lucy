import time
from speak import Speak as s
import speech_recognition as sr
class Mic:
    def __init__(self):
         self.r = sr.Recognizer()
         self.r.dynamic_energy_threshold = 1
    def listen(self):
     try:
         with sr.Microphone() as source:
             audio = self.r.adjust_for_ambient_noise(source)
             source.dynamic_energy_threshold = 1
             while 1:
                 try:
                     audio = self.r.listen(source, timeout=8.0, phrase_time_limit=4)
                 except sr.WaitTimeoutError:
                     print("in sleep")
                     while 1:
                         try:
                             audio = self.r.listen(source, timeout=4.0, phrase_time_limit=4)
                         except sr.WaitTimeoutError:
                             print("In sleep in sleep")
                             continue
                         try:
                             text = self.r.recognize_google(audio)
                             if text in 'Hey lucy':
                                 s.say('at your service , sir')
                                 audio = self.r.listen(source, timeout=5.0, phrase_time_limit=4)
                                 break
                             else:
                                 print("in sleep in sleep no listen said ")
                         except sr.UnknownValueError:
                             s.say('sir im unable to understand')  # s.say('what sir')
                         except LookupError:  # speech is unintelligible
                             s.say('sir im unable to understand')  # s.say('what sir')
                         except IndexError:
                             s.say('sir my speech system r offline')
                         except sr.RequestError:
                             s.say('sir my speech system r offline let me reconnect')
     except:
         print("error")
         pass

    def convert_audio_to_text(self,audio):
     try:
         text = self.r.recognize_google(audio)
         if text is not None:
             return text
         else:
             return None
     except sr.UnknownValueError:
         s.say('what sir now')
     except LookupError:  # speech is unintelligible
         s.say('what sir')
     except IndexError:
         s.say('sir my speech system r offline')
     except KeyError:
         s.say("quota maxed out")
     except sr.RequestError:
         s.say('sir my speech system r offline let me reconnect')
         time.sleep(8)
     except OSError:
         s.say("sir i think , your microphone  haas been disconnected")
    def mics(self):
        pass

   # get audio from the microphone
    @staticmethod
    def mic():
     text=input("enter")
     return text

if __name__ =="__main__":
     print(Mic().listen())
     print("hello")
     
