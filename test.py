def test(limb = "right"):
    ns = "ExternalTools/" + limb + "/PositionKinematicsNode/IKService"
    iksvc = rospy.ServiceProxy(ns, SolvePositionIK)
    ikreq = SolvePositionIKRequest()
    hdr = Header(stamp=rospy.Time.now(), frame_id='base')
    poses = {
        'right': PoseStamped(
            header=hdr,
            pose=Pose(
                position=Point(
                    x=0.450628752997,
                    y=0.261615832271,
                    z=0.317447307078,
                ),
                orientation=Quaternion(
                    x=0.704020578925,
                    y=0.710172716916,
                    z=0.00244101361829,
                    w=0.00194372088834,
                ),
            ),
        ),
    }
    # Add desired pose for inverse kinematics
    ikreq.pose_stamp.append(poses[limb])
    # Request inverse kinematics from base to "right_hand" link
    ikreq.tip_names.append('right_hand')
    resp = iksvc(ikreq)	
    rospy.loginfo("------------------")
    rospy.loginfo(resp.joints)
    # reformat the solution arrays into a dictionary
    joint_solution = dict(zip(resp.joints[0].name, resp.joints[0].position))
    # set arm joint positions to solution
    arm = intera_interface.Limb(limb)
    while not rospy.is_shutdown():
        arm.set_joint_positions(joint_solution)
        rospy.sleep(0.01)


def main():
    """RSDK Inverse Kinematics Example

    A simple example of using the Rethink Inverse Kinematics
    Service which returns the joint angles and validity for
    a requested Cartesian Pose.

    Run this example, the example will use the default limb
    and call the Service with a sample Cartesian
    Pose, pre-defined in the example code, printing the
    response of whether a valid joint solution was found,
    and if so, the corresponding joint angles.
    """
    rospy.init_node("rsdk_ik_service_client")
    
    test()


if __name__ == '__main__':
    main()
