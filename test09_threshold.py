
import cv2

gray = cv2.imread("bookpage.jpg", cv2.IMREAD_GRAYSCALE)

# 这是二值化的阈值，10表示小于10的像素点会被设置为0，大于等于10的像素点会被设置为255，固定阈值，最简单的阈值
ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
# 这是自适应阈值化，把图片分成很多小块，每个小块都有自己的阈值，适合光照不均匀的图片
binary_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 115, 1)
# 这是大金法阈值化，自动计算最优阈值，使得两个类的类间方差最大化，适合图像中有明显的前景和背景
ret1, binary_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("gray", gray)
cv2.imshow("binary", binary)
cv2.imshow("binary_adaptive", binary_adaptive)
cv2.imshow("binary_otsu", binary_otsu)

cv2.waitKey()
