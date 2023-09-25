import cv2

path = "imgprocessing_test.png "
img = cv2.imread(path)
cv2.imshow("img ", img)
dim = img.shape
print(dim)
resized = cv2.resize(img,(900,200)) # width,height
cv2.imshow("resized", resized)





cv2.waitKey(0)
cv2.destroyAllWindows()
