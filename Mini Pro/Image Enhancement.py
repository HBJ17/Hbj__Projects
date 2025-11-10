#Image Enhancement
import cv2


#reading the image
img = cv2.imread("D:\Studies\PycharmProjects\PythonProject\Images\yyyy.jpg")

#preperation of clahe
clahe = cv2.createCLAHE()

#convert gray to scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#apply enhancement
enh_img = clahe.apply(gray_img)

#save it to file
cv2.imwrite("D:\Studies\PycharmProjects\PythonProject\Images\Enhanced.jpg",enh_img)

print("Done Enhancing")

