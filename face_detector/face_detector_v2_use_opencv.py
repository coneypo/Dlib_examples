# created at 2017-11-27
# updated at 2018-09-06

# Author:   coneypo
# Dlib:     http://dlib.net/
# Blog:     http://www.cnblogs.com/AdaminXie/
# Github:   https://github.com/coneypo/Dlib_examples

# create object OpenCv
# use OpenCv to read and show images

import dlib
import cv2

# 使用 Dlib 的正面人脸检测器 frontal_face_detector
detector = dlib.get_frontal_face_detector()

# 图片所在路径
img = cv2.imread("../imgs/faces_2.jpeg")

# 使用 detector 检测器来检测图像中的人脸
faces = detector(img, 1)
print("人脸数 / faces in all：", len(faces))

for i, d in enumerate(faces):
    print("第", i+1, "个人脸的矩形框坐标：",
          "left:", d.left(), '\t', "right:", d.right(), '\t', "top:", d.top(),'\t',  "bottom:", d.bottom())
    cv2.rectangle(img, tuple([d.left(), d.top()]), tuple([d.right(), d.bottom()]), (0, 255, 255), 2)

cv2.namedWindow("img", 2)
cv2.imshow("img", img)
cv2.waitKey(0)
