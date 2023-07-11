
from speak import Speak as s
import os
from command import cd
import webbrowser
import time
from google import search
from datetime import datetime
from move import move
from mic import Mic


##########
def output(st):
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BOARD) 
        GPIO.setwarnings(False)
        path='C:/Users/Ehson Miraz/Desktop/zoook/trigger'
        s1=st.split(" ")
        for i in s1:
          path+='/'+i
        path1=path 
        
      
        t=s1[len(s1)-2]
        if len(s1)>2:
          s2=st.split(" ")
          s2.remove(t)
        else:
            s2=s1
        print(s1)   
        if all( i in cd.time for i in s1):
          d=str(datetime.now())
          
          d=d.split(" ")
          s.say(d[1])
          
        elif all( i in cd.date for i in s1):      
          d=str(datetime.now())
          d=d.split(" ")
          s.say(d[0])
     
        elif "where is" in st:
          data = st.split(" ")
          location = data[2]
          s.say("Hold on sir, I will show you where " + location + " is.")
          webbrowser.open_new_tab("https://www.google.nl/maps/place/" + location + "/&amp;")   
        elif 'what is' in st and 'time' not in st and 'date' not in st and 'your name' not in st:
           print("wait s")
           
        elif all( i in cd.how for i in s1):
           s.say("i am fine")
             
        elif all( i in cd.shut for i in s2):
             sec=str(s1[len(s1)-1])
             if type(t) is not int:
                 t=5
             
             t=str(t)
             sat="sir . i am going to shutdown . in "+ t + "second"
             print(sat)
             s.say(sat)
             t=int(t)
             for i in range(t,1,-1):
                 s.say(str(i))
             os.system("shutdown -h now" )

        elif all( i in cd.rast for i in s1):
             s.say("sir . i am going to . restart the system")
             os.system('reeboot now')
        elif all( i in cd.sleep for i in s1):
             if type(t) is not int:
                 t=5
             s.say("sir m going to sleep in %t sec" %t)
             time.sleep(int(t))
        elif all( i in cd.hi for i in s1):
             s.say("hello sir . how can i . help you")
        elif 'Facebook' in st or 'fb' in st:
            webbrowser.open_new_tab("https://www.facebook.com")

        elif 'send' in st and 'email' in st:
            from lucy.skills.gmail import Mail
            Mail.emails()
            
        elif 'maker' in st:
            s.say(' sir ehson miraz created me')
        elif 'you' and 'born' in st:
            s.say('i was born , on 8 december , same day my maker , was born')
        elif 'do you like' in st:
            choice=st[11:len(st)]
            
            que='i love'+ choice
            s.say(que)
        elif 'name' in st:
                s.say('my name is zook')
        elif 'about you' in st:
             s.say('my name is zook . i am a home assistant robot . i work on 64 bit . micro computer raspberry pi 3 . i have 1 gb ram . 16 gb rom . my main programming , is based on python3 , programming language , which is written , by my maker sir ehson ')
            
        
             s.say('i am having , whole wikipedia .  which can tell you , anything , and also i have whole , you tube . i can send email , to any one . i can manage your facebook messages.')
             
             s.say('how many marks , out of ten , will u give me , sir ')
             i=Mic.mic()
             s.say('thanku sir , impressive')
             
        elif 'play' in st and 'do you' not in st:
            ip=st[5:len(st)]
            for url in search(ip, stop=2):
              
              url1=url
              break
            webbrowser.open(url1)
            d=input("stop or not")
            if d in 'stop it stop the song stop song':
                    os.system('pkill chromium')
        elif 'who is' in st or 'what is' in st and 'name' not in st:
            thing=st[6:len(st)]
            s.say('searching sir')
            import wikipedia
            sen=wikipedia.summary(thing,sentences=1)
            s.say(sen)
            
        elif 'quit'in st or 'Quit' in st or 'quick' in st or 'Quick' in st :
               GPIO.cleanup()
               f
        elif 'this is' in st:
              person='hello'+(st[7:len(st)]) +'nice to meet u i am zook'
              s.say(person)        
               
        elif 'human' in st:
            s.say('all human are my friends')
            s.say('sir ehson taught me that')
            s.say('humanity comes before science and relegion both')
            
            s.say('i will try to live with humans')
        
        elif st in "start walking start moving its show time":
           move.move()
         
        #elif os.path.isdir(path):
          #path+='/zook.py'  
          #f=open(path,'r')
          #cmd=f.read()
          #f.close()          
          #cmd='python C:/Users/Ehson Miraz/Desktop/zoook/command/'+cmd+'.py'          
          #os.system(cmd)

        else:
         s.say("i have no answer sir")
                

         
        
#######



  
