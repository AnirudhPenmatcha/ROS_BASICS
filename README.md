# ROS_BASICS

If you'd like a cheat sheet of sorts that can help make your life easier with using ROS -- then do check out the pdf file("Notes on applying some of ROS's features.pdf") part of this repo. This("README.md") doesn't describe in too much detail about what's there in this repository since there actually isn't much to mention aside from having a look at my notes if you'd like, however, if you read the 'About' of this repository and are interested in trying out this "something cool" that I mentioned, you can clone this repositroy into your computer, copy the package "robot_tutorials" into your ROS workspace, build the package and follow these steps:

**All of this was done in Ubuntu 18.04 LTS using ROS Melodic Morenia so I can't assure whether you have all the required installations/dependencies, but anyways there's no harm really in trying it out.**

Run all these commands in separate terminals:
1. `roscore`
2. `sudo -s` because mouseData_publish.py needs to access your mouse input which requires root user's permission.
3. `rosrun robot_tutorials mouseData_publish.py`
4. `rosrun robot_tutorials mouse_clicks_server.py`
5. `rosrun robot_tutorials mouse_clicks_client.py`

Now try left clicking or right clicking and observe what happens.
