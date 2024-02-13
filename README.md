# YOLO v5 detection on Ouster Lidar 

#### Running aunch file
Clone repository
```
mkdir -p <catkin_ws>/src
git clone https://github.com/laurenbramblett/ouster_yolo_detection
cd <catkin_ws>
catkin build
source ~/<catkin_ws>/devel/setup.bash
```
This was built to run with a specific local python executable. Please fix the shebang line at the top of `detection_msgs/src/server.py` and `yolov5_ouster/detect_ouster_ros.py` if running on your own computer
```
roslaunch detection_msgs detection_launch.launch
```

If you need to change the parameters such as confidence_threshold or whether you want to view the opencv image, change the defaults in `yolov5_ouster/detect_ouster_ros.py` in the `parse_opt()` function



TODO: fix arguments in launch file
