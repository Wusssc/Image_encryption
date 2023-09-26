import cv2

dogkey = cv2.imread("dogkey.png",0)
hidedog = cv2.imread("hidedog.png",0)

dog_new = cv2.bitwise_xor(dogkey,hidedog)

cv2.imshow("dog_new",dog_new)
cv2.imwrite("dog_new.png",dog_new)
cv2.imshow("dogkey",dogkey)
cv2.imshow("hidedog",hidedog)

cv2.waitKey(0)   
cv2.destroyAllWindows()
