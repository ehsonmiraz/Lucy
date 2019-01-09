class move:
 import RPi.GPIO as gpio
 import time
 def move():
  import RPi.GPIO as gpio
  import time
    
  def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(5, gpio.OUT)
    gpio.setup(3, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(7, gpio.OUT)
 
  def forward():
    init()
    gpio.output(7,False)
    gpio.output(3,False)
    gpio.output(5,True)   
    gpio.output(11,True)
    
    #gpio.cleanup()
 
  def right():
   init()
   gpio.output(5, False)
   gpio.output(7, False) 
   gpio.output(11, True)
   gpio.output(3, True)
   time.sleep(2)
   gpio.cleanup()
   forward()
  def left():
   init()
   gpio.output(3, False)
   gpio.output(11, False) 
   gpio.output(5, True)
   gpio.output(7, True)
   time.sleep(2)
   gpio.cleanup()
   forward()
  def backward():
   init()
   gpio.output(5, False)
   gpio.output(11, False) 
   gpio.output(3, True)
   gpio.output(7, True)
    
  def stop():
    gpio.cleanup()
  
  print("walk")
  forward()
  while 1:
      a=input("turn")
      if a in "turn right":
          right()
      elif a in "turn left":
          left()
      elif a in "now stop":
          stop()
      elif a in "move forward move straight go ahead":
          forward()
      elif a in "turn backward step back turn back":
          backward()
      elif a in "return done":
          return
          
   
      
     
