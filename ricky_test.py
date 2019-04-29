#!/usr/bin/env python
import rospy
from geometry_msgs.msg import (
    PoseStamped,
    Pose,
    Point,
    Quaternion,
)
from std_msgs.msg import Header
from sensor_msgs.msg import JointState

from intera_core_msgs.srv import (
    SolvePositionIK,
    SolvePositionIKRequest,
)
import intera_interface
import os
import ricky_movement as rm
import cv2
from cascade_detection import RunPictureIdentifier as rpi
from os.path import expanduser

home = expanduser("~")

def main():
    rospy.init_node("rsdk_ik_service_client")
    joint_angle = {'right_j6': -2.78641015625, 'right_j5': 2.0551220703125, 'right_j4': -0.1027412109375,
            'right_j3': -0.4030029296875, 'right_j2': 0.0948330078125, 'right_j1': -0.1065146484375,
            'right_j0': -0.2461318359375}

    rm.open_gripper()

    intera_interface.Limb('right').move_to_joint_positions(joint_angle)
    # search
    # pickup mortar and place in bed
    # rm.read_from_json(home + '/ros_ws/src/json/ready_pickup.json')
    #
    # # taking a picture
    # img = gp.takePicture()
    # img = cv2.imread(img)
    # # find mortars
    # mortar_pos = rpi.cascade_img(img)
    # # if none try again
    # while mortar_pos != None:
    #     img = gp.takePicture()
    #     img = cv2.imread(img)
    #     mortar_pos = rpi.cascade_img(img)
    #     rospy.sleep(10)
    # # if found set mortar position to first
    # mortar_pos = mortar_pos[0]
    # height, width, channels = img.shape
    # # move arm to grab
    # move_to(mortar_pos, width/2, 0.1)
    # rm.read_from_json(home + '/ros_ws/src/json/pickup_mortar.json')
    rm.read_from_json(home + '/ros_ws/src/json/pickup.json')
    rm.read_from_json(home + '/ros_ws/src/json/movements.json')
    # read the text from each twist
    for i in range(0, 1):
        rm.read_from_json(home + '/ros_ws/src/json/twist.json')
    # remove mortar from bed
    rm.read_from_json(home + '/ros_ws/src/json/pull_out.json')


def move_to((x, y, w, h), arm_x, bound):
    # Gets the horizontal center of the given rectangle
    center = x + (w / 2)
    x = -1
    if center > arm_x:
        center = center - arm_x
        x = 1

    center_ratio = center / arm_x
    move_y = center_ratio * bound * x
    rm.move_relative(position={'x': 0, 'y': move_y, 'z': 0})


if __name__ == '__main__':
    main()
