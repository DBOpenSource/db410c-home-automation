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
if len(sys.argv) > 1:
    XML_PATH = sys.argv[1]
else:
    print "Error: XML path not defined"
    sys.exit(1)

# Init the Cascade Classifier
# http://docs.opencv.org/modules/objdetect/doc/cascade_classification.html#cascadeclassifier
faceCascade = cv2.CascadeClassifier(XML_PATH)

# Init webcam
# http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-videocapture
vc = cv2.VideoCapture(DEVICE_NUMBER)

# Check if the webcam init was successful
# http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-isopened
if vc.isOpened(): # try to get the first frame
    # http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-read
    retval, frame = vc.read()
else:
    sys.exit(1)

# If webcam read successful, loop indefinitely
i = 0
while retval:
    # Define the frame which the webcam will show
    frame_show = frame

    if i%5 == 0:
        # Convert frame to grayscale
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect objects and return an array of faces
        # http://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html#cascadeclassifier-detectmultiscale
        faces = faceCascade.detectMultiScale(
            frame,
            scaleFactor=1.2,
            minNeighbors=2,
            minSize=(50, 50),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        # http://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html#rectangle
        cv2.rectangle(frame_show, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Show the image on the screen
    # http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#imshow
    cv2.imshow("DB410c Workshop #6: Facial Detection", frame_show)

    # Grab next frame from webcam
    retval, frame = vc.read()

    # Exit program after waiting for a pressed key
    # http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#waitkey
    if cv2.waitKey(1) == 27:
        break

    i += 1
