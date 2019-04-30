#This script powers on a GoPro object and utilizes it to take photos and process it through OpenCV

from PIL import Image
import glob
import numpy as np
from goprocam import GoProCamera
from goprocam import constants
import os
import cv2

gpCam = GoProCamera.GoPro()
cascade = cv2.CascadeClassifier('cascade.xml')

#Take power on camera, take picutre, download image, load image
def main():
    power_on()
    take_picture()
    dl_image()
    load_image()


def power_on():
    gpCam.power_on()


def power_off():
    gpCam.power_off()


def take_picture():
        gpCam.take_photo(5)

def dl_image():
    gpCam.downloadLastMedia()



#Gopro API stores last downloaded image into folder where current project is stored.
def load_image():
    for img in glob.glob("change to main folder e.g. c:/users/desktop/ricky"):
        cv_img = cv2.imread(img)
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    grenade = cascade.detectMultiScale(gray)

    for (x, y, w, h) in grenade:
        cv2.rectangle(cv_img, (x, y), (x + w, y + h), (255, 255, 0), 2)


        newimg = cv2.resize(cv_img, (1600, 900))
        cv2.imshow('img', newimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if  __name__ == '__main__':
    main()



