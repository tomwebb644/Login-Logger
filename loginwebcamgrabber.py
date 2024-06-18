# -*- coding: utf-8 -*-
"""
Webcam image grabber

@author: tomwebb
"""
from time import sleep
import cv2 as cv

from pygrabber.dshow_graph import FilterGraph

def get_available_cameras() :

    devices = FilterGraph().get_input_devices()

    available_cameras = {}

    for device_index, device_name in enumerate(devices):
        available_cameras[device_index] = device_name

    return available_cameras

def select_cam(camera_dict):
    for index, cam_name in camera_dict.items():
        if cam_name == "Anker PowerConf C300":
            return index
    return "error"


def getFrame(my_height, my_width, cam_index):
    cam = cv.VideoCapture(cam_index, cv.CAP_MSMF)
    cam.set(3, 1920)
    cam.set(4, 1080)
    _, frame = cam.read()
    cam.release()
    return frame
    
def getIndex():
    with open(r"C:/Users/tomwe/Desktop/LoginLog/login.log", 'r') as fp:
        currentIndex = len(fp.readlines())
    return currentIndex

def saveFrame(outputFile, frame):
    cv.imwrite(outputFile, frame)
    
def run():
    camera_dict = get_available_cameras()
    cam_ind = select_cam(camera_dict)
    if cam_ind == "error":
        print ("Anker cam not detected. Quitting.")
        exit()
    frame = getFrame(1080,1920, cam_ind)
    currentIndex = getIndex()
    outputFile=("C:/Users/tomwe/Desktop/LoginLog/Login_Images/loginUser{}.jpg".format(currentIndex))
    saveFrame(outputFile, frame)
    
run()