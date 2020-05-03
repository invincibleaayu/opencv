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
gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow("gussian",blurred)
#taking xero as 3rd agrument it will calculate the mean automatically
#simple thresholding
(t,thresh)=cv2.threshold(blurred,155,255,cv2.THRESH_BINARY)
cv2.imshow("threshold binary",thresh)
(t,threshInv)=cv2.threshold(blurred,155,255,cv2.THRESH_BINARY_INV)
cv2.imshow("thresholdinv binary",threshInv) 
cv2.imshow("omly coins",cv2.bitwise_and(gray,gray,mask=threshInv))
cv2.waitKey(0)
cv2.destroyAllWindows()
#adaptive thresholding
thresh=cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,4)
cv2.imshow("adaptive mean",thresh)
thresh=cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,4)
cv2.imshow("adaptive gaussian",thresh)
cv2.imshow("only coins",cv2.bitwise_and(gray,gray,mask=thresh))
cv2.waitKey(0)

