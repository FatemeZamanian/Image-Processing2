import numpy as np
import cv2
pp = []
p1 = 0
for i in range(5):
    pp.append(cv2.imread('1/' + str(i + 1) + '.jpg'))
    pp[i] = cv2.cvtColor(pp[i], cv2.COLOR_RGB2GRAY)
    pp[i] = pp[i] // 5
    p1 += pp[i]

pp = []
p2 = 0
for i in range(5):
    pp.append(cv2.imread('2/' + str(i + 1) + '.jpg'))
    pp[i] = cv2.cvtColor(pp[i], cv2.COLOR_RGB2GRAY)
    pp[i] = pp[i] // 5
    p2 += pp[i]

pp = []
p3 = 0
for i in range(5):
    pp.append(cv2.imread('3/' + str(i + 1) + '.jpg'))
    pp[i] = cv2.cvtColor(pp[i], cv2.COLOR_RGB2GRAY)
    pp[i] = pp[i] // 5
    p3 += pp[i]

pp = []
p4 = 0
for i in range(5):
    pp.append(cv2.imread('4/' + str(i + 1) + '.jpg'))
    pp[i] = cv2.cvtColor(pp[i], cv2.COLOR_RGB2GRAY)
    pp[i] = pp[i] // 5
    p4 += pp[i]

a = cv2.hconcat([p1, p2])
b = cv2.hconcat([p3, p4])
c = cv2.vconcat([a, b])
c = cv2.resize(c, (500, 500))

cv2.imshow('Black hole', c)
cv2.waitKey()
