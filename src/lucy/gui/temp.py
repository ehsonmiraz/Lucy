from multiprocessing import Process, Pipe,Value,Queue

from lucy.utils.Enumerations import FaceExEnum
from face_ex import FaceEx, FaceExEngine


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