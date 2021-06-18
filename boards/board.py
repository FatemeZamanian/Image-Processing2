import cv2
org=cv2.imread('board - origin.bmp')
tst=cv2.flip(cv2.imread('board - test.bmp'),1)
org=cv2.cvtColor(org,cv2.COLOR_RGB2GRAY)
tst=cv2.cvtColor(tst,cv2.COLOR_RGB2GRAY)
res = cv2.subtract(tst, org)*3
res=cv2.resize(res,(500,500))
cv2.imshow('board',res)
cv2.waitKey()
