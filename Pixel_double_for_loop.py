import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)

prev_frame_time = 0
new_frame_time = 0

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    maxVal = 0
    maxLoc = (0, 0)

    # Manually finding the brightest spot
    for y in range(gray.shape[0]):  # Rows
        for x in range(gray.shape[1]):  # Columns
            if gray[y, x] > maxVal:
                maxVal = gray[y, x]
                maxLoc = (x, y)

    cv2.circle(frame, maxLoc, 10, (255, 0, 0), 2)

    # Calculating the fps and display on screen
    new_frame_time = time.time()
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    fps_text = f'FPS: {fps:.2f}'
    cv2.putText(frame, fps_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Show frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
