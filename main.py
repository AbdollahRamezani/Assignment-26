import cv2   

my_image = cv2.imread("image.jpg") 
my_image2 = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)   

print(my_image2.shape)  

print(my_image2[10, 15])  

my_image2[10, 15] = 0

my_image2[10:15, 12:20] = 0

image3 = my_image2[320:500, 335:515]
my_image2[0:180, 0:180] = image3

cv2.imshow("title name image", my_image2)
cv2.waitKey()

cv2.imwrite("image2.jpg", my_image2)