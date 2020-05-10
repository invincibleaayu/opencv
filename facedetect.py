from PIL import Image
import face_recognition
import argparse
import cv2
import numpy as np
#fetching the argument and saving it in dictionary
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required= True , help="Enter path to image")
args = vars(ap.parse_args())
#load and showing the image into numpy array
#printing th required data
image=cv2.imread(args["image"])
face_locations=face_recognition.face_locations(image)
print("i found {} faces in the photograph".format(len(face_locations)))
for face_location in face_locations:
    top,right,bottom,left=face_location
    print(" A face is located at  Top:{} Bottom: {} left:{} right:{}".format(top,bottom,left,right))
    face_image=image[top:bottom,left:right]
    pil_image=Image.fromarray(face_image)
    pil_image.show()
