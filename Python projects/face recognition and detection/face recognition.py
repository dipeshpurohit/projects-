#Face recognition

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import face_recognition as fr
import cv2
import os

# open a window to select an image
Tk().withdraw()
load_image = askopenfilename()
# loading and encoding the faces.
target_image = fr.load_image_file(load_image)
target_encoding = fr.face_encodings(target_image)
# Searches for occurrences of this face
def loading_faces(folder):
    encoding_faces = []
    for filename in os.listdir(folder):
        known_image = fr.load_image_file(f'{folder}{filename}')
        known_encoding = fr.face_encodings(known_image)[0]
        encoding_faces.append((known_encoding, filename))
    return encoding_faces
# find faces from known folders
def find_face():
    face_location = fr.face_locations(target_image)
    for person in loading_faces('known/'):
        encoded_face = person[0]
        filename = person[1]
        is_target_face = fr.compare_faces(encoded_face, target_encoding, tolerance=0.5)
        if face_location:
            face_number = 0
            for location in face_location:
                if is_target_face[face_number]:
                    label = filename
                    frame(location, label)
                face_number += 1

# create rectangle and text on the recognized face
def frame(location, label):
    top, right, bottom, left = location
    cv2.rectangle(target_image, (left, top), (right, bottom), (0, 128, 0), 2) # rectangle shape and color
    cv2.putText(target_image, label, (left - 30, bottom + 14), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255, 255), 1) # text shape and color
# displays the image
def recognized():
    image = cv2.cvtColor(target_image, cv2.COLOR_BGR2RGB)
    cv2.imshow('Face recognition', image)
    cv2.waitKey(0)
# closing windows
find_face()
recognized()
