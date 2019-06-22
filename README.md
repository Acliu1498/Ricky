# Ricky

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

- Ubunutu Xenial *THIS VERSION MUST BE USED
- ROS Kinetic *THIS VERSION MUST BE USED
- Python 3

This workstation setup [guide](http://sdk.rethinkrobotics.com/intera/Workstation_Setup) can be followed to install all the necessary prerequisites.

### Installing
First, ensure that Ricky is in sdk mode. To do that this guide [here](http://sdk.rethinkrobotics.com/intera/Upgrade_Sawyer_to_Intera_SDK#Switch_Robot_from_Intera_MFG_to_SDK_Mode) can be followed.
Once done, Ricky's screen should look like this:
![Image Not Found](http://sdk.rethinkrobotics.com/intera/a/images/thumb/9/9e/Sawyer_SDK_Robot_Screen.png/400px-Sawyer_SDK_Robot_Screen.png)

Second, setup the correct networking requirements to interface with Ricky, to do so follow the guide [here](http://sdk.rethinkrobotics.com/intera/Networking).

Finally, create a new catkin package within the ros_ws folder created in the intera workstation setup and place all of the python files within this repository in there. 

## Running the code on ricky

To run your program on ricky first ensure that you are correctly networking with ricky by checking this guide [here](http://sdk.rethinkrobotics.com/intera/Networking) under the direct network configuration section

From there open a new terminal instance and enter the follwing commands:
```
# enter your ros workspace
cd ros_ws
# start the intera script
.\intera.sh
```
After that run your code by opening a new terminal instance and enter the following commands:
```
cd ros_ws

rosrun *name of ricky catkin package* *name of desired program*
```

## Authors

* **Alex Liu** - *Initial work* - [Acliu1498](https://github.com/Acliu1498)
* **Jared Bitanga** - *Initial work* - [BWallStreet](https://github.com/BWallStreet)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

