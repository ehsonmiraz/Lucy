class cap:
 def capture(name):    
  import cv2
  import os
  import time
  from speak import speak as s
  
  cam = cv2.VideoCapture(0)
  detector=cv2.CascadeClassifier('facerec/haarcascade_frontalface_default.xml')#'/home/ehson/Desktop/k/facerec/opencv-files/haarcascade_frontalface_alt.xml')

  Id=str(len(open("facerec/faces.txt",'r').read().split("*")))
  sampleNum=0
  os.makedirs("facerec/training-data/"+name+Id)
  while(True):
    ret, img1 = cam.read()
    img=cv2.flip(img1,1)
    cv2.imshow("l",img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',img)
    try:
      faces = detector.detectMultiScale(gray, 1.3, 5)
    except cv2.error:
      print
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        #incrementing sample number 
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        
        print("facerec/training-data/"+name+Id+"/User"+ str(sampleNum) + ".jpg")
        cv2.imwrite("facerec/training-data/"+name+Id+"/User"+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
        while 0:
          print("hell")
          try:
           ret, img1 = cam.read()
           img=cv2.flip(img1,1)
           cv2.imshow('frame',img)
           break
          except cv2.error:
              s.say('cant see')
              continue
          if cv2.waitKey(100) & 0xFF == ord('q'):
             break
    #wait for 100 miliseconds 
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    elif sampleNum>10:
        break
    

  cam.release()
  f=open("facerec/faces.txt",'a')
  f.write('*'+name)
  f.close()
  cv2.destroyAllWindows()

 if __name__=='__main__':
    capture(input("enter name"))
