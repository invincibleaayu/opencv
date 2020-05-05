from matplotlib import pyplot as plt
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
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
blurred=cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow("blurred image",blurred)
cannydetected=cv2.Canny(blurred,30,150)
cv2.imshow("cannyedge detection",cannydetected)
cv2.waitKey(0)