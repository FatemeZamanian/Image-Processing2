import cv2
pp=[]
p=0
for i in range(15):
    pp.append(cv2.imread('h'+str(i)+'.jpg'))
    pp[i]=cv2.cvtColor(pp[i],cv2.COLOR_RGB2GRAY)
    pp[i]=pp[i]//15
    p+=pp[i]

cv2.imshow('X2',p)
cv2.waitKey()