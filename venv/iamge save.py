
import cv2

# using imread('path') and 0 denotes read as  grayscale image
#img = cv2.imread(r'C:\Users\fcbba\Downloads\opencv-master\opencv-master\samples\data/1.png', 1)
img = cv2.imread('1.png',1)
# This is using for display the image
cv2.imshow('image', img)

m=cv2.waitKey(0)  # This is necessary to be required so that the image doesn't close immediately.
# It will run continuously until the key press.
if m==63:
    cv2.destroyAllWindows()
elif m == ord('l'):
    cv2.imwrite("aa.jpg", img)
    cv2.destroyAllWindows()




