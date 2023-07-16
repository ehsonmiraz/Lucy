import math
import sys
import pygame
import pygame.camera
import pygame.image
from datetime import datetime, timedelta
from multiprocessing import  Queue,Process
from lucy.services.news import NewsGenerator
from lucy.enumerations import FaceExEnum
from lucy.core.console import ConsoleManager as cm
from lucy.settings import  FACE_EX_CONFIG
red = (255,0,0)
blue = (40,150,203)
green = (0,255,0)
yellow = (25,255,40)
white = (255,255,255)
black = (15,10,25)
purple = (136,71,188)
brown = (72, 36, 0)
PI=math.pi

class PyGameEngine():
    def __init__(self):
        self.pg_engine=pygame
        self.pg_engine.init()
        self.cam=self.pg_engine.camera
        self.cam.init()
        self.clock = self.pg_engine.time.Clock()
        cm.console_output("fps: "+str(self.clock.get_fps()))
        self.screenTitle = "Graphics Shapes"
        # Creates a screen to draw upon
        screenSize = (480, 320)
        self.screen = pygame.display.set_mode(screenSize)
        self.pg_engine.display.set_caption(self.screenTitle)
        self.pg_engine.display.flip()
        self.screen.fill(black)
        self.myfont = pygame.font.SysFont('arial', 17)
        self.pg_engine.font.init()


class FaceEx(PyGameEngine):

    rect1 = pygame.Rect(40, 40, 25, 50)
    rect2 = pygame.Rect(40, 100, 30, 30)
    def __init__(self,func_choice=FaceExEnum.SMILE):
        super().__init__()
        self.screenSize = (480, 320)
        self.c=0
        self.news = NewsGenerator().get_news()
        self.base_line=1
        self.lower_jawline=60
        self.lower_eyeline=89.3
        self.eye_pos=0.3
        self.eye_speed=FACE_EX_CONFIG.get('eye_speed')
        self.lips_speed=FACE_EX_CONFIG.get('lips_speed')
        self.func_choice=func_choice

    def check_for_quit(self):
        for event in self.pg_engine.event.get():
           if event.type ==self.pg_engine.QUIT:
              self.quit()
    def quit(self):
        self.pg_engine.display.quit()

    def get_fps(self):
        fps=0.0
        while fps == 0:
            self.clock.tick(30)
            fps = self.clock.get_fps()
        return fps

    def smile(self,point=0,point2=0,ss=0,sp=0,clock=24):
      self.pg_engine.draw.circle(self.screen, blue,(150,95) , 60)
      self.pg_engine.draw.circle(self.screen, blue,(330,95) , 60)
      self.pg_engine.draw.circle(self.screen, black,(150,95+((int)(point2))), 40)
      self.pg_engine.draw.circle(self.screen, black,(330,95+((int)(point2))), 40)
      #pygame.draw.circle(screen, white,(240,80), 4)
      self.pg_engine.draw.arc(self.screen, white, [187-ss,184+point/2 -ss,100+ss,80+ss], 8*PI/7,(13*PI/7),5)
      self.pg_engine.draw.arc(self.screen, white, [191-ss,189+point/2 -ss,93+ss,78+ss], 6*PI/5,1.787*PI,5)
      if ((int)(self.c)==len(self.news)):
          self.c=0
      textsurface = self.myfont.render(self.news[1+(int)(self.c):65+(int)(self.c)], False, (255, 230, 250))
      self.screen.blit(textsurface,(10,275))
      self.c=self.c+0.23
      self.pg_engine.display.update()
      self.pg_engine.time.wait(clock)
    def talk(self):
        x=0
        while x<=self.lower_jawline:
         self.smile(x)
         self.pg_engine.display.update()
         self. screen.fill(black)
         x+=self.lips_speed
        x=0
        while(x<=self.lower_jawline):
         self.smile(self.lower_jawline - x)#,-y2+s2)
         self.screen.fill(black)
         x+=self.lips_speed
    def thanku(self):

        x=self.eye_pos
        while(x<self.lower_eyeline):
             self.smile(0.0,x)
             self.screen.fill(black)
             x+=self.eye_speed

        self.pg_engine.time.wait(100)

        while(x>=self.eye_pos):
             self.smile(0,x)
             self.screen.fill(black)
             x-=self.eye_speed
        funcno=0
    def rec(self,duration=5):
      cameras = self.cam.list_cameras()
      print( "Using camera %s ..." % cameras[1])
      webcam = self.cam.Camera(cameras[0])
      #webcam = self.cam.Camera(cameras[1])
      webcam.start()
      img = webcam.get_image()
      current_time=datetime.now()
      end_time=datetime.now()+timedelta(seconds=duration)
      while  current_time<= end_time :
           self.check_for_quit()
           # draw frame
           self.screen.blit(img, (0,0))
           pygame.display.update()

           # grab next frame
           img = webcam.get_image()
           current_time=datetime.now()
      self.func_choice=FaceExEnum.SMILE
    def laugh(self):
        x = 0
        while x <= self.lower_jawline/2:
            self.smile(x,clock=10)
            self.pg_engine.display.update()
            self.screen.fill(black)
            x += self.lips_speed
        x = 0
        while (x <= self.lower_jawline / 2):
            self.smile(self.lower_jawline / 2 - x, clock=10)  # ,-y2+s2)
            self.screen.fill(black)
            x += self.lips_speed




class FaceExEngine:
  func_choice=FaceExEnum.SMILE
  @classmethod
  def set_choice(cls, func_queue):
      if (func_queue is None):
          print("queue is none")
          return

      if (func_queue is not None and func_queue.qsize() > 0):
          choice = func_queue.get()
          cls.func_choice = choice
  @classmethod
  def run(cls,face_ex_queue=None):
        face_ex=FaceEx()
        while True:
             function_choices={
               FaceExEnum.SMILE:face_ex.smile,
               FaceExEnum.THANK_YOU:face_ex.thanku,
               FaceExEnum.LAUGH:face_ex.laugh,
               FaceExEnum.TALK:face_ex.talk,
               FaceExEnum.REC:face_ex.rec,
               FaceExEnum.QUIT:face_ex.quit
                              }
             cls.set_choice(face_ex_queue)

             if(cls.func_choice):
                function_choices[cls.func_choice]()
             face_ex.screen.fill(black)
             face_ex.check_for_quit()

if __name__ == '__main__':
        try:
            q=Queue()
            q.put(FaceExEnum.THANK_YOU)
            p=Process(target=FaceExEngine.run,args=(q,))
            p.start()
        except Exception as e:
            print("error occured: "+str(e))
            print (sys.exc_info())
            pygame.display.quit()

