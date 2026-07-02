# 图像的梯度，如果有梯度的变化说明图像中有边缘的存在，那么就可以通过梯度的变化来检测图像中的边缘
import cv2

#直接读取灰度图像
gray = cv2.imread("opencv_logo.jpg", cv2.IMREAD_GRAYSCALE)

# laplacian算子可以用来检测图像的边缘，laplacian算子是二阶导数算子，计算图像的二阶导数，二阶导数可以检测图像的边缘
laplaction = cv2.Laplacian(gray, cv2.CV_64F)
# Canny算子
canny = cv2.Canny(gray, 100, 200)

cv2.imshow("gray", gray)    
cv2.imshow("laplaction", laplaction)
cv2.imshow("canny", canny)
cv2.waitKey(0)