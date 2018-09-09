# created at 2017-11-27
# updated at 2018-09-06

# Author:   coneypo
# Dlib:     http://dlib.net/
# Blog:     http://www.cnblogs.com/AdaminXie/
# Github:   https://github.com/coneypo/Dlib_examples

# create object of OpenCv
# use OpenCv to read and show images

import dlib
import cv2

# 使用 Dlib 的正面人脸检测器 frontal_face_detector
detector = dlib.get_frontal_face_detector()

# 图片所在路径
<<<<<<< HEAD:face_detector/face_detector_v2_use_opencv.py
img = cv2.imread("../imgs/faces_2.jpeg")
=======
# read image
img = cv2.imread("imgs/faces_2.jpeg")
>>>>>>> d60b16a6a7a3398853cb4757f39fcdf6d9679f2f:face_detector_v2_use_opencv.py

# 使用 detector 检测器来检测图像中的人脸
# use detector of Dlib to detector faces
faces = detector(img, 1)
<<<<<<< HEAD:face_detector/face_detector_v2_use_opencv.py
print("人脸数 / faces in all：", len(faces))
=======
print("人脸数 / Faces in all: ", len(faces))
>>>>>>> d60b16a6a7a3398853cb4757f39fcdf6d9679f2f:face_detector_v2_use_opencv.py

# Traversal every face
for i, d in enumerate(faces):
    print("第", i+1, "个人脸的矩形框坐标：",
          "left:", d.left(), '\t', "right:", d.right(), '\t', "top:", d.top(),'\t',  "bottom:", d.bottom())
    cv2.rectangle(img, tuple([d.left(), d.top()]), tuple([d.right(), d.bottom()]), (0, 255, 255), 2)

cv2.namedWindow("img", 2)
cv2.imshow("img", img)
cv2.waitKey(0)
