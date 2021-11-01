# ROS_BASICS

This file doesn't describe in too much detail about what's there in this repository since there actually isn't much to mention, however, if you read the description of this repository and are interested in trying out this "cool usage" that I mentioned, you can clone this repositroy into your computer, build the package and follow these steps:

**All of this was done in Ubuntu 18.04 LTS using ROS Melodic Morenia so I can't assure whether you have all the required installations/dependencies, but anyways there's no harm really in trying it out.**

Run all the steps in separate terminals:
1. Run "roscore"
2. In another terminal run "sudo -s", because mouseData_publish.py needs to access your mouse input which requires root user's permission.
3. rosrun robot_tutorials mouseData_publish.py
4. rosrun robot_tutorials mouse_clicks_server.py
5. rosrun robot_tutorials mouse_clicks_client.py

Now try left clicking or right clicking and observe what happens.
