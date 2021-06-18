import cv2
import numpy as np
org=cv2.imread('Mona_Lisa.jpg')
org=cv2.cvtColor(org,cv2.COLOR_RGB2GRAY)
(r,c)=org.shape
l=np.zeros((r,c),dtype='uint8')
color=30

for i in range(r):
    for j in range(c):
        if org[i,j]==0:
            org[i,j]=1

for i in range(c):
    if color<200 and i%2==0:
        color+=1
    l[0:r,i:i+1]=color

res=org/l

cv2.imshow('',res)
cv2.waitKey()