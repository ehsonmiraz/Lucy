import RPi.GPIO as gpio
import time
from lucy.core.console import ConsoleManager as cm
from lucy.engines.stt import STTEngine
from lucy.engines.tts import TTSEngine
from settings import *
class Move:

  def __init__(self):
    self.sttEngine=STTEngine()
    gpio.setmode(gpio.BOARD)
    gpio.setup(LEFT_WHEELS_FORWARD, gpio.OUT)
    gpio.setup(RIGHT_WHEELS_FORWARD, gpio.OUT)
    gpio.setup(RIGHT_WHEELS_BACKWARD, gpio.OUT)
    gpio.setup(LEFT_WHEELS_BACKWARD, gpio.OUT)
 
  def forward(self):
    gpio.output(LEFT_WHEELS_BACKWARD,False)
    gpio.output(RIGHT_WHEELS_BACKWARD,False)
    gpio.output(RIGHT_WHEELS_FORWARD,True)   
    gpio.output(LEFT_WHEELS_FORWARD,True)
    cm.console_output("Moving Forward.....",refresh_console=True)

 
  def right(self):

   gpio.output(LEFT_WHEELS_BACKWARD, False)
   gpio.output(RIGHT_WHEELS_FORWARD, False) 
   gpio.output(LEFT_WHEELS_FORWARD, True)
   gpio.output(RIGHT_WHEELS_BACKWARD, True)
   cm.console_output("Turning Left.....", refresh_console=True)
   time.sleep(TURNING_TIME)
   gpio.cleanup()
   self.forward()

  def left(self):
   gpio.output(RIGHT_WHEELS_BACKWARD, False)
   gpio.output(LEFT_WHEELS_FORWARD, False) 
   gpio.output(RIGHT_WHEELS_FORWARD, True)
   gpio.output(LEFT_WHEELS_BACKWARD, True)
   cm.console_output("Turning Right.....", refresh_console=True)
   time.sleep(TURNING_TIME)
   gpio.cleanup()
   self.forward()

  def backward(self):
   gpio.output(LEFT_WHEELS_FORWARD, False)
   gpio.output(RIGHT_WHEELS_FORWARD, False) 
   gpio.output(RIGHT_WHEELS_BACKWARD, True)
   gpio.output(LEFT_WHEELS_BACKWARD, True)
   cm.console_output("Moving backward.....", refresh_console=True)
    
  def stop(self):
   try:   
    gpio.cleanup()
    cm.console_output("Stoppped", refresh_console=True)
   except Exception as e:
       cm.console_output("restarting....", refresh_console=True)


  def run(self):
   self.forward()
   while True:
      query=self.sttEngine.recognize_input()
      if query in "turn right":
          self.right()
      elif query in "turn left":
          self.left()
      elif query in "now stop":
          self.stop()
      elif query in "move forward move straight go ahead":
          self.forward()
      elif query in "turn backward step back turn back":
          self.backward()
      elif query in "return done":
          self.stop()
          break

if __name__=='__main__':
  Move().run()
  print("moving")
      
     
