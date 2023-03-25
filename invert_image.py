import cv2

image = cv2.imread("girl1.jpg")
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
# print(image2.shape)

for i in range(645):
    for j in range(645):
            image2[i, j] = 255 - image2[i, j]  
            
                  
cv2.imshow("girl", image2)
cv2.imwrite("girl2.jpg", image2)
cv2.waitKey()