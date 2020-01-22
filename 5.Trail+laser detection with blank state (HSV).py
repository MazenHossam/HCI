import cv2
import numpy as np
import argparse
import time

cap = cv2.VideoCapture(0)

pts = []
while (1):

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(11,11),cv2.BORDER_DEFAULT)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    if maxVal > 170:
        cv2.circle(frame, maxLoc, 20, (255, 0, 0), 2, cv2.LINE_AA)
        for i in range(1, len(pts)):
            cv2.line(frame, pts[i], pts[i-1],(0, 0, 255), 3)
            cv2.circle(frame, pts[i],1,(0,0,255))
    pts.append(maxLoc)
    if len(pts) > 40:
        pts.pop(0)

    cv2.imshow('tracker', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()