import cv2
import mediapipe as mp

# Global variable to control the video loop
video_running = True
window_name = 'Little Dance Copiers'

def run():
    global video_running
    video_running = True
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    # Initialize MediaPipe Pose
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    # Initialize drawing utility
    mp_drawing = mp.solutions.drawing_utils

    # Check if camera opened successfully
    if not cap.isOpened(): 
        print("Unable to read camera feed")


    while video_running:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            # Convert the BGR image to RGB
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the image and draw poses on it
            result = pose.process(rgb_image)
            if result.pose_landmarks:
                mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Display the resulting frame
            cv2.imshow(window_name, frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # When everything done, release the video capture and video write objects
    cap.release()

    # Closes all the frames
    cv2.destroyWindow(window_name)

def stop():
    global video_running
    video_running = False