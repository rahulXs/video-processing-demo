import cv2

#0,1,2... webcam indices, for video file pass its path
video=cv2.VideoCapture(0)
a=0
while True:
    a=a+1
    check, frame=video.read()

    print(check)
    print(frame)
    cv2.imshow("Vid capturing",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

print("total stills captured: ",a)
video.release()
cv2.destroyAllWindows