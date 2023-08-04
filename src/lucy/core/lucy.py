
from speak import speak as s
import os
from command import cd
import webbrowser
import time
from google import search
import RPi.GPIO as GPIO
from datetime import datetime
from lucy.core.lucy import move
from mic import mic
from f2 import express as ex
import multiprocessing as mp
from facerec.recognise import Recognise as rec
from facerec.dataset import cap
#####vars
global funcno

##########
def output(st):
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BOARD) 
        GPIO.setwarnings(False)
        path='C:/Users/Ehson Miraz/Desktop/zoook/trigger'
        if st is None:
          s.respond('listening system are offline connect the mic')
          time.sleep(10)
          return 
        s1=st.split(" ")
        for i in s1:
          path+='/'+i
        path1=path 
        
      
        t=s1[len(s1)-2]
        nm=open('facerec/faces.txt','r').read()
        if len(s1)>2:
          s2=st.split(" ")
          s2.remove(t)
        else:
            s2=s1
        print(s1)   
        if all( i in cd.time for i in s1):
          d=str(datetime.now())
          
          d=d.split(" ")
          s.respond(d[1])
          
        elif all( i in cd.date for i in s1):      
          d=str(datetime.now())
          d=d.split(" ")
          funcno.value=3
          s.respond(d[0])
          funcno.value=0
        elif "akbar" in st:
             s.respond("i dont know who is this")
        elif "bat" in st:
                s.respond("this is ADNAN")
        elif "record" in st:
           funcno.value=4
           time.sleep(12)
           funcno.value=0
        elif "where is" in st and 0:
          data = st.split(" ")
          location = data[2]
          funcno.value=3
          s.respond("Hold on sir, I will show you where " + location + " is.")
          funcno.value=0
          webbrowser.open_new_tab("https://www.google.nl/maps/place/" + location + "/&amp;")   
        elif 'what is' in st and 'time' not in st and 'date' not in st and 'your name' not in st:
         
           print("wait s")
           
        elif all( i in cd.how for i in s1):
           funcno.value=3
           s.respond("i am fine")
           funcno.value=0  
        elif all( i in cd.shut for i in s2):
             sec=str(s1[len(s1)-1])
             if type(t) is not int:
                 t=5
             
             t=str(t)
             funcno.value=3
             
             sat="sir . i am going to shutdown . in "+ t + "second"
             print(sat)
             
             s.respond(sat)
             funcno.value=0
             t=int(t)
             for i in range(t,1,-1):
                 funcno.value=3
                 s.respond(str(i))
             
             os.system("sudo shutdown -h now" )

        elif all( i in cd.rast for i in s1):
             funcno.value=3
             s.respond("sir . i am going to . restart the system")
             funcno.value=0
             os.system('reboot now')
        elif all( i in cd.sleep for i in s1):
             if type(t) is not int:
                 t=5
             funcno.value=3
             s.respond("sir m going to sleep in %t sec" %t)
             time.sleep(int(t))
             funco.value=0
        elif all( i in cd.hi for i in s1):
             funcno.value=3
             s.respond("hello sir . how can i help you")
             funcno.value=0
             funcno.value=1
        elif 'Facebook' in st or 'fb' in st:
            webbrowser.open_new_tab("https://www.facebook.com")

        elif 'send' in st and 'email' in st:
            from gmail import mail
            mail.emails()
            funcno.value=1
            
        elif 'maker' in st:
            funcno.value=3
            s.respond(' sir ehson miraz created me')
            funcno.value=0
        elif 'you' and 'born' in st:
            funcno.value=3    
            s.respond('i was born , on 8 december , same day my maker , was born')
            funcno.value=0
        elif 'do you like' in st:
            choice=st[11:len(st)]
            funcno.value=3
            que='i love'+ choice
            s.respond(que)
            funcno.value=0
        elif 'name' in st:
                funcno.value=3
                s.respond('my name is LUCY')
                funcno.value=0
        elif 'about you' in st:
             funcno.value=3
             s.respond('my name is LUCY . i am a home assistant robot . i work on 64 bit . micro computer raspberry pi 3 . i have one gigabyte ram . sixteen gigabyte rom . my main programming , is based on python3 , programming language , which is written , by my maker sir ehson ')
            
        
             s.respond('i am having , whole wikipedia .  which can tell you , anything , and also i have whole , you tube . i can send email , to any one . i can manage your facebook messages.')
             
             s.respond('how many marks , out of ten , will u give me , sir ')
             funcno.value=0
             #i=mic.mic()
             time.sleep(5)
             funcno.value=3 
             s.respond('thanku sir , impressive')
             funcno.value=0
             funcno.value=1
             
             
        elif 'play' in st and 'do you' not in st:
            ip=st[5:len(st)]
            for url in search(ip, stop=2):
              
              url1=url
              break
            webbrowser.open(url1)
            d=input("stop or not")
            if d in 'stop it stop the song stop song':
                    os.system('pkill chromium')
        
        elif (('who is' in st) or( 'what is' in st ))and ('name' not in st) and (st[6:len(st)] not in nm) and 'this' not in st : 
            thing=st[6:len(st)]
            s.respond('searching sir')
            import wikipedia
            sen=wikipedia.summary(thing,sentences=1)
            funcno.value=3
            s.respond(sen)
            funcno.value=0
            funcno.value=1
        elif 'who is' in st or 'ognise' in st:
                         #tells who is in front than u shud ask who is"name he told of the person in front of the camera"
           name=rec.recog()     
           s.respond(name)
           name=name[8:]
           '''
           faces=(open('facerec/faces.txt').read().split('**')).index(name)
           
           dis=open('facerec/bio.txt','r')   
           for i in range(1,faces):
               try:                                                          
                line=dis.readline()                                                       

                if name in line[0:20] :                  
                     s.respond(line[21:len(line)+1])
                     break
               except Exception as e:
                 break
               try: 
                s.respond(dis.readLine())
               except Exception as e:
                    s.respond("name not found")
                    continue   '''
        elif 'quit'in st or 'Quit' in st or 'quick' in st or 'Quick' in st :
               GPIO.cleanup()
               funcno.value=5
               f
        elif 'this is' in st:
              identity=(st[7:len(st)])
              open('facerec/faces.txt','a').write(identity)
              welcome='hello'+identity +'nice to meet u i am LUCY'
              funcno.value=3
              s.respond(welcome)
              s.respond("scanning  , face")
              funcno.value=0
              cap.capture(identity)
              funcno.value=3
              s.respond('tell me something about'+ identity)
              funcno.value=0
              dis=identity + ' '*(20-len(identity))+mic.mic()
              biodata=open('facerec/bio.txt','a')
              biodata.write(dis)
              biodata.write('\n')
              biodata.close()
        elif 'human' in st:
            funcno.value=3
            
            s.respond('all human are my friends')
            s.respond('sir ehson taught me that')
            s.respond('humanity comes before science and relegion both')
            
            s.respond('i will try to live with humans')
            funcno.value=0
        elif st in "start walking start moving its show time":
           move.move()
         
        #elif os.path.isdir(path):
          #path+='/LUCY.py'  
          #f=open(path,'r')
          #cmd=f.read()
          #f.close()          
          #cmd='python C:/Users/Ehson Miraz/Desktop/zoook/command/'+cmd+'.py'          
          #os.system(cmd)

        else:
         funcno.value=3       
         s.respond("i have no answer sir")
         funcno.value=0       
         funcno.value=1
         
        
#######



  


#######
funcno=mp.Value('i')
funcno.value=0
p = mp.Process(target=ex.face, args=(funcno,))
p.start()
'ex.face(0)'
print("pr on")
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)

#right=11
#forward=7
#left=5
led=32
flash=16
s.respond("power on")

s.respond("g p i o system , online")
s.respond('main system , online')
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,1)
GPIO.setup(flash,GPIO.OUT)
os.system('aplay repulsar.wav')



print("hello")
while True:
  print("mic")     
  a=mic.mic()
  print("no prob mic")
  output(a)
  
