#!/usr/bin/env python
import cv2, sys
import numpy as np

# Constants
DEVICE_NUMBER = 0
FONT_FACES = [
    cv2.FONT_HERSHEY_SIMPLEX,
    cv2.FONT_HERSHEY_PLAIN,
    cv2.FONT_HERSHEY_DUPLEX,
    cv2.FONT_HERSHEY_COMPLEX,
    cv2.FONT_HERSHEY_TRIPLEX,
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX
]
MOTION_THRESHOLD = 0.3

# Init webcam
# http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-videocapture
vc = cv2.VideoCapture(DEVICE_NUMBER)

# Check if the webcam init was successful
# http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-isopened
if vc.isOpened(): # try to get the first frame
    # http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-read
    retval, frame = vc.read()
    previous_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
else:
    sys.exit(1)

# If webcam read successful, loop indefinitely
while retval:
    # Define the frame which the webcam will show
    frame_show = frame

    # Convert frame to grayscale to make phase comparison
    # http://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html#cvtcolor
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert frames into floating point
    f_frame = np.float32(frame)
    f_previous_frame = np.float32(previous_frame)

    # Run a phase correlation
    # http://docs.opencv.org/2.4/modules/imgproc/doc/motion_analysis_and_object_tracking.html#phasecorrelate
    (dx,dy) = cv2.phaseCorrelate(f_frame,f_previous_frame)

    # Determine motion from the phase correlation
    if abs(dx) > MOTION_THRESHOLD and abs(dy) > MOTION_THRESHOLD:
        # Write some text onto the frame
        # http://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html#puttext
        font_typeface = FONT_FACES[5]
        font_scale = 2
        font_color = (0,0,255)
        font_weight = 5
        x = 0
        y = 50
        cv2.putText(frame_show, "Motion!", (x,y), font_typeface, font_scale, font_color, font_weight)


    # Show the image on the screen
    # http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#imshow
    cv2.imshow("DB410c Workshop #5: Motion Detection", frame_show)

    # Retain previous frame for comparison
    previous_frame = frame
    # Grab next frame from webcam
    retval, frame = vc.read()

    # Exit program after waiting for a pressed key
    # http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#waitkey
    if cv2.waitKey(1) == 27:
        break
