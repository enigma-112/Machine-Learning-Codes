# Reading a video stream from camera (Frame by Frame)

import cv2

x = cv2.VideoCapture(0) # id for default webcam is 0

while True : 
	ret,frame = x.read()
	gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	if ret==False :
		continue

	cv2.imshow("Video Frame", frame)
	cv2.imshow("Gray Frame", gray_frame)

	# Enter q to quit 

	key_pressed = cv2.waitKey(1) & 0xFF

	if key_pressed == ord('q'):
		break

# when everythig is done release the camera

x.release()
cv2.destroyAllWindows()

