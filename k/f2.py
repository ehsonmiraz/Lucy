import math
import sys
import time
import pygame
import pygame.camera
import pygame.image


class Face:
    a = -1
    global c
    c = 0

    def face(funcno):
        global news
        news = ""

        pygame.camera.init()
        pygame.init()

        cameras = pygame.camera.list_cameras()

        print("Using camera %s ..." % cameras[0])

        webcam = pygame.camera.Camera(cameras[0])
        wc = 0
        rect1 = pygame.Rect(40, 40, 25, 50)
        rect2 = pygame.Rect(40, 100, 30, 30)

        # colors
        red = (255, 0, 0)
        blue = (40, 150, 203)
        green = (0, 255, 0)
        yellow = (25, 255, 40)
        white = (255, 255, 255)
        black = (15, 10, 25)
        purple = (136, 71, 188)
        brown = (72, 36, 0)

        # sizes
        global screenSize
        screenSize = (480, 320)
        # t

        # clock

        global clock
        clock = pygame.time.Clock()
        clock.tick(30)

        # PI
        global PI
        PI = math.pi

        # vars
        def makenews():
            global news
            # url = 'https://www.ndtv.com/latest?pfrom=home-topnavigation/'#'https://www.ndtv.com/topic/parse'
            news = open('news.txt', 'r').read()

        global a
        makenews()
        screenTitle = "Graphics Shapes"
        # Creates a screen to draw upon
        screen = pygame.display.set_mode(screenSize, pygame.FULLSCREEN)
        pygame.display.set_caption(screenTitle)
        screen.fill(black)

        def quitting():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()

        def Quit():
            pygame.display.quit()

        def talk():
            x2 = 1
            y2 = 0.4
            for i in range(1, 50):
                smile(x2)
                # pygame.display.update()
                screen.fill(black)
                x2 += 1.5
                y2 += 0.1
            s = x2
            s2 = y2
            x2 = 1
            for i in range(1, 50):
                smile(-x2 + s)  # ,-y2+s2)

                # pygame.display.update()
                screen.fill(black)
                x2 += 1.5
                y2 += 0.1

        # Make a smiley face
        def thanku():

            y2 = 0.3
            for i in range(1, 48):
                smile(0.0, y2)
                # pygame.display.update()
                screen.fill(black)

                y2 += 0.9

            s2 = y2
            y2 = 2
            time.sleep(0.4)
            for i in range(1, 48):
                smile(0, -y2 + s2)
                # pygame.display.update()
                screen.fill(black)

                y2 += 0.9

            funcno.value = 0

        myfont = pygame.font.SysFont('arial', 17)
        pygame.font.init()
        c = 0

        def smile(point=0, point2=0, ss=0, sp=0):
            global c
            global news
            global webcam
            global wc
            if wc == 1:
                webcam.stop()
                wc = 0
            pygame.draw.circle(screen, blue, (150, 95), 60)
            pygame.draw.circle(screen, blue, (330, 95), 60)
            pygame.draw.circle(screen, black, (150, 95 + ((int)(point2))), 40)
            pygame.draw.circle(screen, black, (330, 95 + ((int)(point2))), 40)
            # pygame.draw.circle(screen, white,(240,80), 4)
            pygame.draw.arc(screen, white, [187 - ss, 184 + point / 2 - ss, 100 + ss, 80 + ss], 8 * PI / 7,
                            (13 * PI / 7), 5)
            pygame.draw.arc(screen, white, [191 - ss, 189 + point / 2 - ss, 93 + ss, 78 + ss], 6 * PI / 5, 1.787 * PI,
                            5)
            if ((int)(c) == len(news)):
                c = 0

            textsurface = myfont.render(news[1 + (int)(c):65 + (int)(c)], False, (255, 230, 250))
            screen.blit(textsurface, (10, 275))

            c = c + 0.23
            pygame.display.update()
            screen.fill(black)

        # (4*PI-12*PI/7), 5)
        a = -1

        def rec():
            global webcam
            global wc
            webcam.start()
            wc = 1
            img = webcam.get_image()
            print('hiil')

            while True:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        sys.exit()
                # draw frame

                screen.blit(img, (0, 0))
                pygame.display.update()
                if funcno.value == 0:
                    break
                # grab next frame
                img = webcam.get_image()

        def laugh():

            # add=(40)
            x2 = 0.3

            for i in range(1, 200):
                smile(x2)
                # pygame.display.update()
                screen.fill(black)
                x2 += 0.3

            s = x2
            x2 = 0.3
            for i in range(1, 200):
                smile(-x2 + s)
                # pygame.display.update()
                screen.fill(black)
                x2 += 0.3

        pygame.display.flip()

        a = -1
        smile()
        while 1:
            functions = [smile, thanku, laugh, talk, rec, Quit]
            # funcnumbr=[ 0,    1,        2     3     4,   5 ]
            functions[funcno.value]()
            # thanku()
            quitting()

    try:
        if __name__ == '__main__':
            face(3)
    except:
        import sys
        import pygame
        print(sys.exc_info())
        pygame.display.quit()
