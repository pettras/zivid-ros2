# Zivid ROS2 driver

This is an unofficial ROS2 driver for [Zivid 3D cameras](https://www.zivid.com/). based of Zivid-ROS1 driver: https://github.com/zivid/zivid-ros

RUN

ros2 launch zivid_camera zivid_camera_standalone.launch.py 
ros2 run rviz2 rviz2 -d /home/kukauser/dev_ws/src/zivid-ros2/zivid_camera/rviz/camera_view.rviz 
ros2 run zivid_samples sample_capture 
