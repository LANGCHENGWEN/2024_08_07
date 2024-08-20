import cv2
camera = cv2.VideoCapture(0)
while True:
    is_success, frame = camera.read()
    if is_success:
        cv2.imshow("Collector", frame)
        cv2.imwrite("image.jpg", frame)
        key = cv2.waitKey(30)
    else:
        print("Wait for camera ready......")
        key = cv2.waitKey(1000)

    if  key == ord('q') or \
        key == ord('Q'):
            break
    
cv2.destroyAllWindows()
