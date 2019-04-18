#!/usr/bin/env python

# Copyright (c) 2013-2018, Rethink Robotics Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import numpy as np

import cv2
from cv_bridge import CvBridge, CvBridgeError

import rospy
import intera_interface
import os
import ricky_movement as rm
from cascade_detection import RunPictureIdentifier as rpi


def find(camera='head_camera', raw=False, edge=False, gain=-1, exposure=-1):
    # rospy.init_node('camera_display', anonymous=True)
    cameras = intera_interface.Cameras()
    if not cameras.verify_camera_exists(camera):
        rospy.logerr("Could not detect the specified camera, exiting the example.")
        return
    cameras.start_streaming(camera)
    rectify_image = not raw
    use_canny_edge = edge

    # optionally set gain and exposure parameters
    if gain is not None:
        if cameras.set_gain(camera, gain):
            rospy.loginfo("Gain set to: {0}".format(cameras.get_gain(camera)))

    if exposure is not None:
        if cameras.set_exposure(camera, exposure):
            rospy.loginfo("Exposure set to: {0}".format(cameras.get_exposure(camera)))

    cameras.set_callback(camera, save_image_callback,
                         rectify_image=rectify_image, callback_args=(use_canny_edge, camera))

    def clean_shutdown():
        print("Shutting down camera_display node.")
        cv2.destroyAllWindows()

    rospy.on_shutdown(clean_shutdown)
    rospy.loginfo("Camera_display node running. Ctrl-c to quit")
    cameras.stop_streaming(camera)
    print('done')


def save_image_callback(img_data, edge_detection):
    bridge = CvBridge()
    try:
        cv_image = bridge.imgmsg_to_cv2(img_data, "bgr8")
    except CvBridgeError, err:
        rospy.logerr(err)
        return
    if edge_detection == True:
        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        # customize the second and the third argument, minVal and maxVal
        # in function cv2.Canny if needed
        get_edge = cv2.Canny(blurred, 10, 100)
        cv_image = np.hstack([get_edge])
    cv2.imwrite('/home/alex/ros_ws/src/intera_sdk/intera_examples/scripts/img/img.png', cv_image)


def read(file_path):
    img = cv2.imread(file_path)
    return rpi.cascade_img(img)


def show(file_path):
    img = cv2.imread(file_path, 0)
    cv2.imshow('img', img)
    cv2.waitKey(3)


def display_img():
    rospy.loginfo(os.path.expanduser('~') + '/ros_ws/test1.png')
    img = cv2.imread(os.path.expanduser('~') + '/ros_ws/test1.png', 0)
    cv2.imshow('test.png', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()