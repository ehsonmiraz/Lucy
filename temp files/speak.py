class speak:
 def say1(text,vol=1.0,rate=130):
   import pyttsx3
   import os
   engine = pyttsx3.init()
   print(engine)
   voi = engine.getProperty('voices')
   engine.setProperty('rate',rate)  
   engine.setProperty('voice', 'english')
   engine.setProperty('volume',vol)
   #text="espeak -ven-us+f3 --stdout"+ " '"+text+"' "+"-a 300 -s 130 | aplay"
   
   #text1='espeak -ven-us+f8 --stdout'+ ' "' +text+'" ' +'-a 400 -s 117 | aplay'
   
   #os.system(text1)
   #print(text1)
   engine.say(text)
   engine.runAndWait()
 def say(text):
     import os
     file=open('/home/pi/Desktop/k/teext.txt' ,'w')
     file.write(text)
     file.close()
     os.system('bash /home/pi/Desktop/k/pico.bash')
     print("done")
       
 if __name__=='__main__':
     say("hey have you watched , avenger infinity wars . You should see it , its a nice movie")#"either, you, die, a ,hero. or. live long and watch yourself becoming a villain -joker")




#CRCJL8Q9
