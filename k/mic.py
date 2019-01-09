class mic:
 #
 def mics():
  import time
  from speak import speak as s
  import speech_recognition as sr  
   # get audio from the microphone                                                                       
  r = sr.Recognizer()
  sr.Recognizer().dynamic_energy_threshold=1
  try:
   with sr.Microphone() as source:
    
    audio = r.adjust_for_ambient_noise(source)
    source.dynamic_energy_threshold = 1
    r.dynamic_energy_threshold = 1
    while 1:
     try:
      audio = r.listen(source,timeout=8.0,phrase_time_limit=4)
     except sr.WaitTimeoutError:
      print("in sleep")   
      while 1:
         try :
          
          audio = r.listen(source,timeout=4.0,phrase_time_limit=4)
         except sr.WaitTimeoutError:
            continue
            print("In sleep in sleep")
         try:
           text=r.recognize_google(audio)
           if text in 'zook zoook zuk hey listen':
              s.say('at your service , sir')
              audio = r.listen(source,timeout=5.0,phrase_time_limit=4)
              break
           else:
               print("in sleep in sleep no listen said ")
         except sr.UnknownValueError:
            print()#s.say('what sir')  
         except LookupError: # speech is unintelligible
           print()#s.say('what sir')
         except IndexError:
           s.say('sir my speech system r offline')
         except sr.RequestError:
           s.say('sir my speech system r offline let me reconnect')
         ''' except sr.WaitTimeoutError:
             print("cnti")
             continue'''
   
     try:
        text=r.recognize_google(audio)
        if text is not None:
         return text
     except sr.UnknownValueError:
      s.say('what sir now')  
     except LookupError: # speech is unintelligible
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

 def mic():
     text=input("enter")
     return text
 if __name__ =="__main__":
   while 1:
     print(mic())
     
