# 图像的梯度
import cv2

#直接读取灰度图像
gray = cv2.imread("opencv_logo.jpg", cv2.IMREAD_GRAYSCALE)

laplaction = cv2.Laplacian(gray, cv2.CV_64F)

cv2.imshow("gray", gray)    
cv2.imshow("laplaction", laplaction)

cv2.waitKey(0)