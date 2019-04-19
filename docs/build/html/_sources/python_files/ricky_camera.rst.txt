ricky_camera.py
==================
This file contains functions that can be called to interact with Ricky's built in cameras. For more information on the interface in which these functions interact you can find more information `here <https://rethinkrobotics.github.io/intera_sdk_docs/5.1.0/intera_interface/html/index.html>`_.

take_picture(camera, raw, edge, gain, exposure)
-----------------------------------------------
This method is can be used to take a picture using the given camera. The location of the image can be found at ~ros_ws/src/intera_sdk/intera_examples/scripts/img/img.png, this location can be changed however by changing the imwrite location in show_image_callback

Parameters:

- camera='head_camera': 
    - The name of the camera you wish to use.
    - This camera must be recognized by the intera sdk
    - To see which cameras are available call list_cameras provided by the intera_interface.camera.Cameras interface
    - If No camera is provided, this function will use the head camera.
- raw=False: 
    - If this values is false the image will be rectified, if true then it will not
    - This value is false by default
- edge=False:
    - If this value is true canny edge detection will be used when taking the picture
    - This value is false by default

