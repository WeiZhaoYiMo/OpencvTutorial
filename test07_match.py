# 模板匹配 template matching
import cv2
import numpy as np

image = cv2.imread("poker.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 转换成灰度图是因为比较的是图片的形状、纹理、亮度等特征，不是颜色

# 使用索引，给定一个区域的图像作为模板
template = gray[75:105, 235:265] # np切片，感觉类似于之前的crop = image[10:170, 40:200]

# cv2.match Template()函数是把gray和tmplate分别标准化，结果不受光照强度影响
match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED) # 返回一张新的图片（相似度矩阵），每个数字表示模板放在这里有多像
locations = np.where(match >= 0.9) # locations是一个元组，里面有两个数组，分别是y坐标和x坐标，表示相似度大于0.9的点的坐标

h, w = template.shape[0:2]
for p in zip(*locations[::-1]): # zip(*locations[::-1])是把locations的两个数组解压缩成x和y坐标，像是拉链一样把x，y缝合起来，[::-1]是把y,x反过来，因为numpy数组是先纵列再横行 
    x1, y1 = p[0], p[1]
    x2, y2 = x1 + w, y1 + h
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow("match", image)
cv2.waitKey()