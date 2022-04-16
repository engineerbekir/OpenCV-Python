# ****Red, Blue, Green and every color except white****


import cv2
import numpy as np

cam = cv2.VideoCapture(0)



while True:

    _, frame = cam.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Red color
    low_red = np.array([150, 130, 60])
    high_red = np.array([179, 255, 255])
    mask_red = cv2.inRange(hsv, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask= mask_red)

    # Blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    mask_blue = cv2.inRange(hsv, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask= mask_blue)
    
    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    mask_green = cv2.inRange(hsv, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask= mask_green)

    # every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv, low, high)
    everyColor = cv2.bitwise_and(frame, frame, mask=mask)


    cv2.imshow("Frame", frame)
    cv2.imshow("Red mask", red)
    # cv2.imshow("Blue mask", blue)
    # cv2.imshow("Green mask", green)
    # cv2.imshow("Every color", everyColor)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cam.release()
cv2.destroyAllWindows()    




