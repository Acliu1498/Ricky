ricky_movement.py
==================

move_to(limb, position,orientation, speed)
------------------------------------------
This function is used to move a given limb to a specified point and orientation using the `IK_service <http://sdk.rethinkrobotics.com/intera/Kinematics_Solvers>`_ provided by the intera sdk.

- limb: 
    - Which one of Ricky's limb's you would like to move
- position: 
    - The 3D ending point of Ricky's limb in the form of a dictionary
    - Example: {'x' = 1.123, 'y' = 0.574, 'z' = 0.234}
- orientation: 
    - The ending quaternion of Ricky's limb in the form of a dictionary
    - Example: {'x' =-0.421, 'y'=1.223, 'z'=0.225, 'w'=0.1132}
- speed: 
    - ratio of how fast the limb should move [0.0-1.0]

move_relative(limb, position, orientation, speed)
-------------------------------------------------
This function is used to move a limb relative to its current position.
Note: this method also uses the IK_Service

- limb: 
    - Which one of Ricky's limb's you would like to move
- position: 
    - The desired change in 3D space from the current point
    - Example: {'x' = 0.1, 'y' = 0.0, 'z' = 0.0}
- orientation: 
    - The desired change in ornamentation of Ricky's limb in the form of a dictionary
    - Example: {'x' =-0.0, 'y'=0.2, 'z'=0.0, 'w'=0.01}
- speed: 
    - ratio of how fast the limb should move [0.0-1.0]

close_gripper()
---------------
This function closes the right_gripper and calibrates it if necessary

open_gripper()
---------------
This function opens the right_gripper and calibrates it if necessary

read_from_json(file)
--------------------
This function parses a given json file. 
For more information refer to the .. _Json_Files: section


