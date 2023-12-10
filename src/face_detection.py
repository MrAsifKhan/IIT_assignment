# importing requried libraries
import cv2
import time
import numpy as np

# loads the opencv haarcascade classifier for face detection(detects only front view)
def load_classifier() -> cv2.CascadeClassifier:
    face_cascade = cv2.CascadeClassifier('src/haarcascade_frontalface_default.xml')
    if face_cascade.empty():
        print("Error: Failed to load the cascade classifier")
        exit()
    return face_cascade

# to calculate the fps
def calculate_fps(start_time: float, frame_count: int, fps: float) -> tuple:
    frame_count += 1
    interval = 1 # only update fps for every 1 second
    elapsed_time = time.time() - start_time
    if elapsed_time > interval:  
        fps = frame_count / elapsed_time
        frame_count = 0
        start_time = time.time()
    return fps, start_time, frame_count

# to display the calculate fps on the frame output
def display_fps(frame: np.ndarray, fps: int) -> None:
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

# perfrom actual face detection using videocapture
def start_face_detection(classifier: cv2.CascadeClassifier, show_fps=True) -> None:
    video_capture = cv2.VideoCapture(0)  # capture video from webcam

    if not video_capture.isOpened():
        print('No video camera found')
        exit()

    if show_fps:  # initializing fps variables
        start_time = time.time()
        frame_count = 0
        fps = 0

    print("press \"q\" key to quit")

    while True:  # start capturing 
        _, frame = video_capture.read()  # read the frame

        desired_width = 300
        desired_height = 300
        resized_frame = cv2.resize(frame, (desired_width, desired_height))

        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

        faces = classifier.detectMultiScale(  # detect the faces
            gray_frame,
            scaleFactor=1.1,
            minNeighbors=7,
            minSize=(20, 20)
        )

        for (x, y, w, h) in faces:  # draw the rectangle around each face
            cv2.rectangle(resized_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if show_fps:
            fps, start_time, frame_count = calculate_fps(start_time, frame_count, fps)
            display_fps(resized_frame, fps)

        cv2.imshow('Face Detection', resized_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # stop if 'q' key is pressed
            break

    video_capture.release()
    cv2.destroyAllWindows()

def main():
    face_cascade = load_classifier()
    start_face_detection(face_cascade)

if __name__ == "__main__":
    main()
