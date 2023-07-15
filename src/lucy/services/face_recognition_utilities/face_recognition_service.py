import json
import pickle
import datetime
import os
import cv2
import face_recognition

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import lucy
from lucy.core.console import  ConsoleManager as cm

class FaceRecognition:
    TOLERANCE = 0.6
    MODEL = "hog"  # cnn
    CURRENT_DIR = os.path.dirname(__file__)

    @classmethod
    def generate_encodings(cls):
        cm.console_output("starting capturing...../")
        # time.sleep(2)
        cap = cv2.VideoCapture(0)
        counter=1
        encodingList = []
        while True:
            success, image = cap.read()
            if (not success):
                cm.console_output("unable to read")
                continue
            cm.console_output(success)
            # if(image)
            image = cv2.resize(image, (480, 360))

            locations = face_recognition.face_locations(image, model=cls.MODEL)
            encodings = face_recognition.face_encodings(image, locations)
            # image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
            if (len(locations) is 0):
                cm.console_output("no face detected")
                time.sleep(2)
                key = cv2.waitKey(10)
                if (key == ord('q') or counter > 10):
                    break
                continue
            face_location = locations[0]
            encoding = encodings[0]

            encodingList.append(encoding)
            cm.console_output("Photo " + str(counter) + " clicked")
            counter += 1
            time.sleep(2)
            key = cv2.waitKey(1)
            if (key == ord('q') or counter > 10):
                break

        cv2.destroyAllWindows()
        cap.release()
        return encodingList
    @classmethod
    def save_encoding(cls,subject,encodings):
        ID=str(datetime.datetime.now())

        with open(os.path.join(cls.CURRENT_DIR, '....', 'files', 'faces_list.json') ,"w") as file:
               faces_list=json.dump(file)
        faces_list.append({
            ID:subject
        })

        with open(os.path.join(cls.CURRENT_DIR, '....', 'files','face_encodings', f'{ID}.pkl') ,"wb") as file :
            pickle.dump(encodings,file)

    @classmethod
    def load_encodings(cls):
        known_faces = []
        known_names = []
        file = open(os.path.join(cls.CURRENT_DIR, '....', 'files', 'faces_list.json'), "w")
        faces_list = json.load(file)

        for ID in faces_list.keys():
            file=open(os.path.join(cls.CURRENT_DIR, '....', 'files', 'face_encodings', f'{ID}.pkl'), "wb")
            encoding=pickle.load(file)

            known_faces.append(encoding)
            known_names.append(faces_list.get(ID))
        return  known_faces,known_names

    def recognise_subject(cls):
        known_faces,known_names=cls.load_encodings()
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            locations = face_recognition.face_locations(image, model=cls.MODEL)
            encodings = face_recognition.face_encodings(image, locations)
            rawCapture.truncate(0)
            print("label 1")
            for face_encoding, face_location in zip(encodings, locations):
                results = face_recognition.compare_faces(known_faces, face_encoding, cls.TOLERANCE)
                match = None

                if True in results:
                    match = known_names[results.index(True)]
                    lucy.output_engine.respond("Match found : " + match)
                else:
                    lucy.output_engine.respond("I dont know yet you can add this face to my database")
    def add_face_to_db(cls,subject):
         encodings=cls.generate_encodings()
         cls.save_encoding(subject,encodings)
         lucy.output_engine.respond(f"saved {subject}'s face to my database")


if(__name__=='__main__'):
    FaceRecognition.add_face_to_db("ehson")