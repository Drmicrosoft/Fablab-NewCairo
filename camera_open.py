import cv2
while 1 :
		
	camera = cv2.VideoCapture(0)
	(grabbed, frame) = camera.read()
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF		
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break



camera.release()
cv2.destroyAllWindows()
