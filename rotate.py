import cv2

img = cv2.imread('sad_mens.jpg')
img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
img = cv2.rotate(img,cv2.ROTATE_180)

cv2.imshow("",img)
cv2.waitKey()

cv2.imwrite('sad_mens2.jpg',img)