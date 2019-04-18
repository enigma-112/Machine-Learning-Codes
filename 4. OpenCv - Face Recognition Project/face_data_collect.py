import cv2
import numpy as np 

# Initializing Webcam
cap = cv2.VideoCapture(0)

# For face detection using  haarcascade classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:

	# Capturing the video frame by frame 
	ret,frame = cap.read()

	if ret==False:
		continue

	

	faces = face_cascade.detectMultiScale(frame,1.3,5)
	print(faces)

	for face in faces:
		x,y,w,h = face
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255), 5)

	cv2.imshow("Face Image",frame)






	key_pressed = cv2.waitKey(1) & 0xFF
	if key_pressed == ord("q"):
		break




cap.release()
cv2.destroyAllWindows()