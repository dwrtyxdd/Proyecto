import cv2

url = 'http://192.168.1.11/capture'
cap = cv2.VideoCapture(url)

winName = 'IP_CAM'
cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)

while(1):
    cap.open(url)

    ret, frame = cap.read()

    if ret:
        #frame = cv2.rotate
        cv2.imshow(winName,frame)
    tecla =cv2.waitKey(1) & 0xFF
    if tecla == 27:
        break
cv2.destroyAllWindows()
