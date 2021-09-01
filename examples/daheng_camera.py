import gxipy as gx
import cv2

if __name__ == "__main__":
    cap = gx.CameraCap(0)
    cv2.namedWindow('', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('', 1920, 1080)
    while True:
        img = cap.read()
        cv2.imshow('', img)
        if cv2.waitKey(1) == 27:
            cap.close()
            break

