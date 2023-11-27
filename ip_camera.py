import cv2

# Replace this URL with the URL provided by your IP camera app
ip_camera_url = '---'

cap = cv2.VideoCapture(ip_camera_url)

while(True):
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('IP Camera Stream', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()