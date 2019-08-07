import cv2

img = cv2.imread("bicycle.jpeg",1)
#img2 = cv2.imread("bicycle.jpeg",cv2.IMREAD_GRAYSCALE)


cv2.imshow("abcd",img)
#cv2.imshow("grary",img2)

cv2.waitKey(0)

cv2.destroyAllWindows()
