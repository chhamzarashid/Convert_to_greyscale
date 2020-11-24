from cv2 import cv2

img=cv2.imread('1.jpg',1)
cv2.imshow("Hamza",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#convert to Greyscale

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("grey.png",grey)
cv2.imshow('image',grey)

cv2.waitKey(0)
cv2.destroyAllWindows()
