import cv2
import face_recognition


cam =  cv2.VideoCapture(1)
color = (0,0,255)

while True:
    ret,frame =cam.read() 
    frame = cv2.flip(frame, 1)

    faceLocations = face_recognition.face_locations(frame)

    for index, faceloc in enumerate(faceLocations):
        topleftY, buttomRightX, buttomRightY, topleftX = faceloc
        pt1 = (topleftX, topleftY)
        pt2 = (buttomRightX, buttomRightY)

        cv2.rectangle(frame, pt1, pt2, color, 2)

        cv2.imshow("FaceDetection in Real Time", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cam.release()
cv2.destroyAllWindows()






