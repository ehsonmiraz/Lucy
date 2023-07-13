import lucy
#import RPi.GPIO as gpio
import time
from lucy.core.console import ConsoleManager as cm
from lucy.engines.stt import STTEngine
from lucy.engines.tts import TTSEngine
from lucy.core.settings import *
class Move:
    @classmethod
    def run(cls):
        print("running")


# class Move1:
#   @classmethod
#   def setup(cls):
#
#     gpio.setmode(gpio.BOARD)
#     gpio.setup(LEFT_WHEELS_FORWARD, gpio.OUT)
#     gpio.setup(RIGHT_WHEELS_FORWARD, gpio.OUT)
#     gpio.setup(RIGHT_WHEELS_BACKWARD, gpio.OUT)
#     gpio.setup(LEFT_WHEELS_BACKWARD, gpio.OUT)
#   @classmethod
#   def forward(cls):
#     gpio.output(LEFT_WHEELS_BACKWARD,False)
#     gpio.output(RIGHT_WHEELS_BACKWARD,False)
#     gpio.output(RIGHT_WHEELS_FORWARD,True)
#     gpio.output(LEFT_WHEELS_FORWARD,True)
#     cm.console_output("Moving Forward.....",refresh_console=True)
#
#   @classmethod
#   def right():
#
#    gpio.output(LEFT_WHEELS_BACKWARD, False)
#    gpio.output(RIGHT_WHEELS_FORWARD, False)
#    gpio.output(LEFT_WHEELS_FORWARD, True)
#    gpio.output(RIGHT_WHEELS_BACKWARD, True)
#    cm.console_output("Turning Left.....", refresh_console=True)
#    time.sleep(TURNING_TIME)
#    gpio.cleanup()
#    Move.forward()
#   @classmethod
#   def left(cls):
#    gpio.output(RIGHT_WHEELS_BACKWARD, False)
#    gpio.output(LEFT_WHEELS_FORWARD, False)
#    gpio.output(RIGHT_WHEELS_FORWARD, True)
#    gpio.output(LEFT_WHEELS_BACKWARD, True)
#    cm.console_output("Turning Right.....", refresh_console=True)
#    time.sleep(TURNING_TIME)
#    gpio.cleanup()
#    Move.forward()
#   @classmethod
#   def backward(cls):
#    gpio.output(LEFT_WHEELS_FORWARD, False)
#    gpio.output(RIGHT_WHEELS_FORWARD, False)
#    gpio.output(RIGHT_WHEELS_BACKWARD, True)
#    gpio.output(LEFT_WHEELS_BACKWARD, True)
#    cm.console_output("Moving backward.....", refresh_console=True)
#
#   @classmethod
#   def stop(cls):
#    try:
#     gpio.cleanup()
#     cm.console_output("Stoppped", refresh_console=True)
#    except Exception as e:
#        cm.console_output("restarting....", refresh_console=True)
#
#   @classmethod
#   def run(cls):
#    Move.setup()
#    Move.forward()
#    while True:
#       query=lucy.sttEngine.recognize_input()
#       if query in "turn right":
#           Move.right()
#       elif query in "turn left":
#           Move.left()
#       elif query in "now stop":
#           Move.stop()
#       elif query in "move forward move straight go ahead":
#           Move.forward()
#       elif query in "turn backward step back turn back":
#           Move.backward()
#       elif query in "return done":
#           Move.stop()
#           break

if __name__=='__main__':
  Move.run()
  print("moving")
      
     
