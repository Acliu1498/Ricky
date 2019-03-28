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
import json
import os
import ricky_movement as rm
import ricky_camera as rc
import ricky_external_camera as rec
import ocr


def main():
    rospy.init_node("rsdk_ik_service_client")
    joint_angle = {'right_j6': -2.78641015625, 'right_j5': 2.0551220703125, 'right_j4': -0.1027412109375,
            'right_j3': -0.4030029296875, 'right_j2': 0.0948330078125, 'right_j1': -0.1065146484375,
            'right_j0': -0.2461318359375}

    rm.open_gripper()


    intera_interface.Limb('right').move_to_joint_positions(joint_angle)
    rm.read_from_json('/home/alex/ros_ws/src/json/movements.json')
    rm.read_from_json('/home/alex/ros_ws/src/json/twist.json')
    rm.read_from_json('/home/alex/ros_ws/src/json/pull_out.json')

    # rm.read_from_json('/home/alex/ros_ws/src/json/pickup.json')
    # rm.read_from_json('/home/alex/ros_ws/src/json/movements.json')
    # text = []
    # for i in range(0, 5):
    #     img = rec.cap_pic()
    #     text.append(ocr.ocr(img))
    #     rm.read_from_json('/home/alex/ros_ws/src/json/twist.json')
    #
    # for line in text:
    #     print(line)


if __name__ == '__main__':
    main()
