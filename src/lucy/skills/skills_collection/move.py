import lucy
import RPi.GPIO as gpio
import time
from lucy.core.console import ConsoleManager as cm
from lucy.engines.stt import STTEngine
from lucy.engines.tts import TTSEngine
from lucy.core.gpio_config import *



class Move:
  @classmethod
  def setup(cls):

    gpio.setmode(gpio.BOARD)
    gpio.setup(LEFT_WHEELS_FORWARD, gpio.OUT)
    gpio.setup(RIGHT_WHEELS_FORWARD, gpio.OUT)
    gpio.setup(RIGHT_WHEELS_BACKWARD, gpio.OUT)
    gpio.setup(LEFT_WHEELS_BACKWARD, gpio.OUT)
  @classmethod
  def forward(cls):
    gpio.output(LEFT_WHEELS_BACKWARD,False)
    gpio.output(RIGHT_WHEELS_BACKWARD,False)
    gpio.output(RIGHT_WHEELS_FORWARD,True)
    gpio.output(LEFT_WHEELS_FORWARD,True)
    cm.console_output("Moving Forward.....",refresh_console=True)

  @classmethod
  def right():

   gpio.output(LEFT_WHEELS_BACKWARD, False)
   gpio.output(RIGHT_WHEELS_FORWARD, False)
   gpio.output(LEFT_WHEELS_FORWARD, True)
   gpio.output(RIGHT_WHEELS_BACKWARD, True)
   cm.console_output("Turning Left.....", refresh_console=True)
   time.sleep(TURNING_TIME)
   gpio.cleanup()
   Move.forward()
  @classmethod
  def left(cls):
   gpio.output(RIGHT_WHEELS_BACKWARD, False)
   gpio.output(LEFT_WHEELS_FORWARD, False)
   gpio.output(RIGHT_WHEELS_FORWARD, True)
   gpio.output(LEFT_WHEELS_BACKWARD, True)
   cm.console_output("Turning Right.....", refresh_console=True)
   time.sleep(TURNING_TIME)
   gpio.cleanup()
   Move.forward()
  @classmethod
  def backward(cls):
   gpio.output(LEFT_WHEELS_FORWARD, False)
   gpio.output(RIGHT_WHEELS_FORWARD, False)
   gpio.output(RIGHT_WHEELS_BACKWARD, True)
   gpio.output(LEFT_WHEELS_BACKWARD, True)
   cm.console_output("Moving backward.....", refresh_console=True)

  @classmethod
  def stop(cls):
   try:
    gpio.cleanup()
    cm.console_output("Stoppped", refresh_console=True)
   except Exception as e:
       cm.console_output("restarting....", refresh_console=True)

  @classmethod
  def run(cls, **kwargs):
   Move.setup()
   Move.forward()
   while True:
      query=lucy.sttEngine.recognize_input()
      if(not query): continue
      if "right" in query  :
          Move.right()
      elif  "left" in query :
          Move.left()
      elif "stop" in query  :
          Move.stop()
      elif "forward" in query or "straight" in query :
          Move.forward()
      elif "backward" in query or "back" in query:
          Move.backward()
      elif "quit" in query  :
          Move.stop()
          break

if __name__=='__main__':
  Move.run()
  print("moving")
      
     
