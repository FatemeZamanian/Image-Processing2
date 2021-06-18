import cv2
x=cv2.imread('a.tif')
y=cv2.imread('b.tif')
x=cv2.cvtColor(x,cv2.COLOR_RGB2GRAY)
y=cv2.cvtColor(y,cv2.COLOR_RGB2GRAY)
x=-x
y=-y
x=x-y
x=cv2.resize(x,(500,500))
cv2.imshow('Happy lier :)', x)
cv2.waitKey()