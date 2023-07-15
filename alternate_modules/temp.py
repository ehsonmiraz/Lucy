from multiprocessing import Process, Queue

from lucy.enumerations import FaceExEnum
from face_ex import FaceExEngine


if __name__ == '__main__':

    func_choice_q=Queue()
    func_choice_q.put(FaceExEnum.TALK)
    #parent_conn, child_conn = Pipe()
    p = Process(target=FaceExEngine.run,args=(func_choice_q,))
    p.start()
    list=[FaceExEnum.SMILE,FaceExEnum.REC,FaceExEnum.THANK_YOU,FaceExEnum.TALK]

    for i in list:
       func_choice_q.put(i)


    p.join()