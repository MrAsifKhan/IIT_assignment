
# Face Detection

An application for detecting faces in real time using webcame based on OpenCV Python.

<img src="https://github.com/MrAsifKhan/IIT_assignment/blob/main/sample_outputs/sample_output.png" alt="sample output" width="200"/>

## Clone the repository:
```bash
git clone https://github.com/MrAsifKhan/IIT_assignment
```

# To run the application follow the procedure accordingly
1. [Linux](#linux)
2. [Docker](#docker)
3. [Windows](#running-application-on-windows)
4. [ROS](#ROS)



## Linux
a. Open terminal and navigate to the project repository
```bash
cd IIT_assignment
```
b. Run the below commands to install application dependency libraries
          
```bash
chmod +x install_opencv  # might be requried to avoid permission related errors
./install_opencv
```

c. Once the required dependencies are installed run the following commands to run the application:
      
```bash
chmod +x check_and_launch  # might be requried to avoid permission related errors
./check_and_launch
```

( Press 'q' key to quit the application )


## Docker 
**Prerequisites:**
- Docker.
### Using Dockerfile:
a. Open terminal and navigate to the Dockerfile inside project repository
```bash
cd IIT_assignment
```
b. Build the docker
```bash
docker build -t <image_name>:<tag> -f docker/face_detection.dockerfile . 
```
c. **Run the built docker:**
```bash
docker run  --rm --privileged --network=host --ipc=host -e DISPLAY=:1 -v /dev*:/dev* -v /tmp/.X11-unix:/tmp/.X11-unix  <image_name>:<tag>
```

 ### Using Docker image:
a. **Download the Docker image:**
```bash
docker pull asifpattan/face_detection:6.5
```

b. **Run the container:**
```bash
docker run  --rm --privileged --network=host --ipc=host -e DISPLAY=:1 -v /dev*:/dev* -v /tmp/.X11-unix:/tmp/.X11-unix  asifpattan/face_detection:6.5
```

**Troubleshoot:**
Sometimes it can happen that the camera might not be foud or the display cannot be accessd. To fix these issues run the below command before running the container to make the devices visible:
```bash
xhost +
```


## Running application on Windows

   To run the face detection application follow the below steps:
   
   a. Make sure python is installed, if not it can be downloaded from https://www.python.org/downloads/
         
Install pip using
      
  ```bash
  pip install pip
  ```
      
   b. Run below command to install requirements from requirements.txt file
      
```bash
cd IIT_assignment
pip install -r requirements.txt
 ```
      
   c. Once the requirements are installed successfully, run the below command to start the application 
      
  ```bash
  python src/face_detection.py
  ```
      
   d. Press 'q' key on keyboard to stop the application

## ROS
**Prerequisites:**
- ROS2.
- Python
- colcon (sudo apt install python3-colcon-common-extensions)
- cv_bridge (sudo apt-get install ros-<dist_name>-cv-bridge)
### Using Dockerfile:
a. Open terminal and navigate to project repository
```bash
cd IIT_assignment
```
b. Run below command to build the ros package
```bash
colcon build
```
c. Once the built is successful, source the package
```bash
source install/setup.bash
```
d. Run the launch file
```bash
ros2 launch image_processing_pkg image_processing.launch.py
```

