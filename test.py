import cv2
from imgProcessing import cv2show, addNoise, gaussian_blur,im2bw,morphThreat,GetContours

cap=cv2.VideoCapture(0)
cap.set(3,900)
cap.set(4,900)

while(cap.isOpened()):
    ret,frame = cap.read()
    # cap.read()返回两个值，第一个值为布尔值，如果视频正确，那么就返回true,  第二个值代表图像三维像素矩阵
    
    frame = gaussian_blur(frame)
    frame = im2bw(frame)
    frame = morphThreat(frame,5,5,10)
    frame = GetContours(frame)
    
    
    cv2.imshow('Capture', frame)
    k=cv2.waitKey(1)
    if k==ord('s'):
        print('222222')
        print(cap.get(3))
        print(cap.get(4))
    elif k==ord('q'):
        print('完成')
        cap.release()
        cv2.destroyAllWindows()
        break
