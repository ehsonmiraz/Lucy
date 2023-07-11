
# coding: utf-8

# Face Recognition with OpenCV

# To detect faces, I will use the code from my previous article on [face detection](https://www.superdatascience.com/opencv-face-detection/). So if you have not read it, I encourage you to do so to understand how face detection works and its Python coding. 



#import numpy to convert python lists to numpy arrays as

import cv2
import numpy as np
import os
from lucy.engines.tts import TTSEngine
class FaceRecognition:
     def __init__(self):
         self.subjects = open('faces.txt', 'r').read().split('*')
         self.faces , self.labels = self.prepare_training_data("training-data")
         self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
         self.face_recognizer.train(self.faces, np.array(self.labels))

     #function to detect face using OpenCV
     def detect_face(self,img):
            # convert the test image to gray image as opencv face detector expects gray images
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # load OpenCV face detector, I am using LBP which is fast
            # there is also a more accurate but slow Haar classifier
            face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')

            # let's detect multiscale (some images may be closer to camera than others) images
            # result is a list of faces
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

            # if no faces are detected then return original img
            if (len(faces) == 0):
                return None, None

            # under the assumption that there will be only one face,
            # extract the face area
            (x, y, w, h) = faces[0]
            # return only the face part of the image
            return gray[y:y + w, x:x + h], faces[0]
     def prepare_training_data(self,data_folder_path):
        #------STEP-1--------
        #get the directories (one directory for each subject) in data folder
        dirs = os.listdir(data_folder_path)
        #list to hold all subject faces
        faces = []
        #list to hold labels for all subjects
        labels = []

        #let's go through each directory and read images within it
        for dir_name in dirs:

            #our subject directories start with letter 's' so
            #ignore any non-relevant directories if any


            #------STEP-2--------
            #extract label number of subject from dir_name
            #format of dir name = slabel
            #, so removing letter 's' from dir_name will give us label
            label = int(dir_name[len(dir_name)-1:])

            #build path of directory containin images for current subject subject
            #sample subject_dir_path = "training-data/s1"
            subject_dir_path = data_folder_path + "/" + dir_name

            #get the images names that are inside the given subject directory
            subject_images_names = os.listdir(subject_dir_path)

            #------STEP-3--------
            #go through each image name, read image,
            #detect face and add face to list of faces
            for image_name in subject_images_names:

                #ignore system files like .DS_Store
                if image_name.startswith("."):
                    continue;

                #build image path
                #sample image path = training-data/s1/1.pgm
                image_path = subject_dir_path + "/" + image_name

                #read image
                image = cv2.imread(image_path)

                #display an image window to show the image
                #cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
                cv2.waitKey(100)

                #detect face
                face, rect =self.detect_face(image)

                #------STEP-4--------
                #for the purpose of this tutorial
                #we will ignore faces that are not detected
                if face is not None:
                    #add face to list of faces
                    faces.append(face)
                    #add label for this face
                    labels.append(label)

        cv2.destroyAllWindows()
        cv2.waitKey(1)
        cv2.destroyAllWindows()

        return faces, labels

     def predict(self,test_img):
        #make a copy of the image as we don't want to chang original image
        img = test_img.copy()
        #detect face from the image
        face, rect = self.detect_face(img)

        #predict the image using our face recognizer
        label, confidence = self.face_recognizer.predict(face)
        #get name of respective label returned by face recognizer
        label_text = self.subjects[label]

        return label_text
     def recognise_face(self):
       while 1:
         cap=cv2.VideoCapture(1)
         ret,imgx=cap.read()

         print("kl")

         try:
          #cv2.imshow("cap",imgx)
          predicted_img ='Name is '+ self.predict(imgx)
          cap.release()
          cv2.destroyAllWindows()
          break
         except cv2.error:
           print("can't see")
           continue
         except Exception as e:
           print("can't see")
           continue

       return predicted_img

     def capture(self,name):
         cam = cv2.VideoCapture(1)
         detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
         Id = str(len(open("faces.txt", 'r').read().split("*")))
         sampleNum = 0
         try:
           os.makedirs("training-data/" + name + Id)
         except Exception as e:
             print(e)
             return

         while (True):
             ret, img1 = cam.read()
             img = cv2.flip(img1, 1)
             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
             try:
                 faces = detector.detectMultiScale(gray, 1.3, 5)
             except cv2.error:
                 print
             for (x, y, w, h) in faces:
                 cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                 # incrementing sample number
                 sampleNum = sampleNum + 1
                 # saving the captured face in the dataset folder

                 print("facerec/training-data/" + name + Id + "/User" + str(sampleNum) + ".jpg")
                 cv2.imwrite("training-data/" + name + Id + "/User" + str(sampleNum) + ".jpg",
                             gray[y:y + h, x:x + w])

             # wait for 100 miliseconds
             if cv2.waitKey(100) & 0xFF == ord('q'):
                 break
             # break if the sample number is morethan 20
             elif sampleNum > 10:
                 break

         cam.release()
         f = open("faces.txt", 'a')
         f.write('*' + name)
         f.close()
         cv2.destroyAllWindows()
if __name__=='__main__':
  print(FaceRecognition().capture("Ehsoon"))








