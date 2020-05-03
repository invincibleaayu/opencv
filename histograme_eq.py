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
eq=cv2.equalizeHist(gray)
cv2.imshow("normal and equilized",np.hstack([gray,eq]))
cv2.waitKey(0)