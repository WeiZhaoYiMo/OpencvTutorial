# 图像绘制图形文字
import cv2
import numpy as np

# 因为图像本质上是numpy数组，所以可以直接创建一个numpy数组表示图像的画布
image = np.zeros([300,300,3], dtype = np.uint8)

cv2.line(image, (100, 200), (250, 250), (255, 0, 0), 2)
cv2.rectangle(image,(30, 100), (60, 150), (0, 255, 0), 2)
cv2.circle(image, (150, 100), 20, (0, 0, 255), 3)
cv2.putText(image, "OpenCV", (100, 50), 0, 1, (255, 255, 255), 2, 1)

cv2.imshow("image", image)
cv2.waitKey()