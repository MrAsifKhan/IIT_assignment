# using ubuntu base image
FROM ubuntu:18.04

WORKDIR /app/

# copying source files
COPY face_detection.py /app/
COPY haarcascade_frontalface_default.xml /app/

# install dependencies
RUN apt update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libopencv-dev python3-opencv

CMD ["python3", "face_detection.py"]
