# ROS_BASICS


1. Run "roscore"
2. In another terminal run "sudo -s", because mouseData_publish.py needs to access your mouse input which requires root user's permission.
3. For publishing the mouse data : rosrun robot_tutorials mouseData_publish.py
4. rosrun robot_tutorials mouse_clicks_server.py
5. rosrun robot_tutorials mouse_clicks_client.py
