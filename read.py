import cv2 as cv

img = cv.imread("cat.jpg")
resized_img = cv.resize(img,None, fx=0.3, fy=0.3,interpolation=cv.INTER_AREA)

cv.imshow("Cat(Resized)",resized_img)
#cv.imshow("Cat BIg Pic",img)
cv.waitKey(0)

