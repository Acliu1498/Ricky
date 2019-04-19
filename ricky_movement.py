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
import ricky_camera as rc


# method to move to a pose given a position and orientation
def move_to(limb, position, orientation, speed):
    rospy.loginfo("Starting move...")
    ns = "ExternalTools/" + limb + "/PositionKinematicsNode/IKService"
    iksvc = rospy.ServiceProxy(ns, SolvePositionIK)
    ikreq = SolvePositionIKRequest()

    poses = new_pose(position, orientation)
    # Add desired pose for inverse kinematics
    ikreq.pose_stamp.append(poses[limb])
    # Request inverse kinematics from base to "right_hand" link
    ikreq.tip_names.append('right_hand')
    resp = iksvc(ikreq)
    # reformat the solution arrays into a dictionary
    joint_solution = dict(zip(resp.joints[0].name, resp.joints[0].position))
    rospy.loginfo(joint_solution)
    # set arm joint positions to solution
    arm = intera_interface.Limb(limb)

    arm.set_joint_position_speed(speed)
    arm.move_to_joint_positions(joint_solution, timeout=5, threshold=0.01)

    rospy.loginfo('Move complete')


# helper method to compare the arm position to the desired position
def compare_poses(arm, pose):
    for attr, value in arm.endpoint_pose()['position'].__dict__.iteritems():
        if not (pose[attr] - 0.02) < value < (pose[attr] + 0.02):
            return False
    return True


# helper methood to compare orientations
def compare_orientations(arm, pose):
    for attr, value in arm.endpoint_pose()['orientation'].__dict__.iteritems():
        if not (pose[attr] - 0.005) < value < (pose[attr] + 0.005):
            return False
    return True


def move_relative(limb='right',
                  position={'x': 0, 'y': 0, 'z': 0},
                  orientation={'x': 0, 'y': 0, 'z': 0, 'w': 0},
                  speed=0.2):
    arm = intera_interface.Limb(limb)
    curr_position = arm.endpoint_pose()['position']
    rospy.loginfo("currpos:" + str(curr_position))
    new_position = {'x': curr_position.x + position['x'],
                    'y': curr_position.y + position['y'],
                    'z': curr_position.z + position['z']}
    rospy.loginfo("newpos:" + str(new_position))
    curr_orientation = arm.endpoint_pose()['orientation']
    new_orientation = {'x': curr_orientation.x + orientation['x'],
                       'y': curr_orientation.y + orientation['y'],
                       'z': curr_orientation.z + orientation['z'],
                       'w': curr_orientation.w + orientation['w']}
    move_to(limb, new_position, new_orientation, speed)


# Method to create a new poses give position and orientation
def new_pose(position, orientation):
    hdr = Header(stamp=rospy.Time.now(), frame_id='base')
    poses = {
        'right': PoseStamped(
            header=hdr,
            pose=Pose(
                position=Point(
                    x=position['x'], #0.450628752997,
                    y=position['y'], #0.161615832271,
                    z=position['z']  #0.317447307078,
                ),
                orientation=Quaternion(
                    x=orientation['x'], #0.704020578925,
                    y=orientation['y'], #0.710172716916,
                    z=orientation['z'], #0.00244101361829,
                    w=orientation['w']  #0.00194372088834,
                ),
            ),
        ),
    }

    return poses


# function to close the gripper
def close_gripper():
    gripper = intera_interface.Gripper('right_gripper')

    # calibrate gripper if necessary
    if not gripper.is_calibrated():
        gripper.calibrate()
    gripper.close()


# function to open the gripper
def open_gripper():
    gripper = intera_interface.Gripper('right_gripper')
    # calibrate gripper if necessary
    if not gripper.is_calibrated():
        gripper.calibrate()
    gripper.open()


''' 
function to read a set of movements from a json file
'''
def read_from_json(file):
    with open(file) as json_file:
        data = json.load(json_file)
        for m in data:
            # moves to a specified point and orientation
            if m['action'] == 'move':
                move_to('right', m["position"], m['orientation'], m['speed'])
            # moves joints to respective positions
            elif m['action'] == 'move_joint':
                intera_interface.Limb('right').move_to_joint_positions(m['joint_angles'])
            # moves relative to its current location
            elif m['action'] == 'move_relative':
                move_relative('right', m['position'], m['orientation'], m['speed'])
            elif m['action'] == 'close_grip':
                close_gripper()
            elif m['action'] == 'open_grip':
                open_gripper()
            elif m['action'] == 'take_pic':
                rc.take_picture(m['camera'])

            if 'comment' in m:
                rospy.loginfo(m['comment'])
