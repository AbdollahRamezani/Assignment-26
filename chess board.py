import cv2

my_image = cv2.imread("background_white.jpg")


for i in range(0, 500, 100):
    for j in range(0, 500, 100):
        my_image[i:i+50, j:j+50] = 0
        my_image[i+50:i+100, j+50:j+100] = 0

  




cv2.imshow("chess board", my_image)
cv2.imwrite("chess board.jpg", my_image)
cv2.waitKey()