from multiprocessing import Process, Queue
import time
from lucy.enumerations import FaceExEnum
from lucy.gui.face_ex import FaceExEngine
from lucy.gui import  current_face_expression
from lucy.gui import  current_face_expression
if __name__ == '__main__':

    # p = Process(target=FaceExEngine.run, args=(current_face_expression.face_ex_queue,))
    # p.start()
    # list=[FaceExEnum.SMILE,FaceExEnum.REC,FaceExEnum.THANK_YOU,FaceExEnum.TALK]
    #
    # for i in list:
    #    current_face_expression.face_ex_queue.put(i)
    #    time.sleep(4)


    p.join()