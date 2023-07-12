class H:
 import timestamp
 a=timestamp.now()
 from facerec.recognise import Recognise as rec
 print(a)
 
 print(rec.recog())
 print(timestamp.now())
