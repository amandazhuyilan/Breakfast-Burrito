## Self-Driving Cars Cheatsheet
[Link to MIT self-driving cars lecture.](https://selfdrivingcars.mit.edu/)

### Levels of Automation 
<img src="https://cdn-images-1.medium.com/max/1600/1*I5vwQqqViZI3QAJ0Dry_cQ.png" width= "400">

- L0: Starting point
- L1, L2, L3: __Human-Centered Autonomy__- AI not fully responsible.
  - When will the features be avaliable? (traffic, highway, sensor-based, etc.)
  - How many seconds until it takes over?
  - Teleoperation support?
  
- L4, L5: __Full Autonomy__- AI is fully responsible.
  - No teleoperation
  - No 10-second rule: It’s allowed to ask for human help, but not guaranteed to ever
receive it.
- Arrive to a safe destination or safe harbor.
- Allow the human to take over when they choose to.


### Sensors 
- Dead Reckoning Sensor: 
  - Uses data from Gyro sensor, Accelerometer, Speed pulse, Wheel speed data of two non-turning wheels.
  - Continues positioning even in the tunnels and urban canyons.
  
- Ultrasonic:
  - High proximity detection, works in extreme weather/light conditions.
  - No color/contrast/texture feedback. Low resolution. Low speed detection.
  
- LIDAR: 
  - Extremely accurate depth information, higher resolution than radar, 360 degrees of visualibility.
  - Expensive. Doesn't work well in extreme weather.
  
- Radar:
  - Cheap, does well in extreme weathers, ability to detect speed.
  - Low resolution, no color or texture features.
  - Used automotive sensor for object detection and tracking
  
- Passive Visual (Camera):
  - Cheap, high resolution, huge data = deep learning. 
  - Bad at depth estimation, noisy in extreme weather.
  - Accuracy based on camera calibration.
  
### [SLAM Simultaneous Localization and Mapping](https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-412j-cognitive-robotics-spring-2005/projects/1aslam_blas_repo.pdf)
The goal of this technology is to use the environment to update the position of the robot.
- Extended Kalman Filter: update where the robot thinks it is based on features(landmarks)


  - No color/contrast/texture feedback. Low resolution. Low speed detection.
