#!/usr/bin/env python
import cv2, sys

# Constants
DEVICE_NUMBER = 0
IMAGE_FILE = "output_with_text.jpg"
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

retval, frame = vc.read()

# Write the filename onto the frame using every font
# http://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html#puttext
for i in xrange(len(FONT_FACES)):
    font_typeface = FONT_FACES[i]
    font_scale = 2
    font_color = (255,255,255)
    x = 0
    y = (i+1)*50
    cv2.putText(frame, IMAGE_FILE, (x,y), font_typeface, font_scale, font_color)

# Save the frame as an image file
# http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#imwrite
cv2.imwrite(IMAGE_FILE, frame)

# Read the output file
# http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#imread
img = cv2.imread(IMAGE_FILE)

# Show the image on the screen
# http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#imshow
cv2.imshow("DB410c Workshop #2: Write Text", img)

# Exit program after waiting indefinitely for a pressed key
# http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#waitkey
cv2.waitKey(0)
