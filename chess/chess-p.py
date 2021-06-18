import cv2
import numpy as np
org=cv2.imread('chess pieces.jpg')

# r=(org.shape[1])//7
# c=org.shape[0]
# for i in range(0,org.shape[1],r):
#     res=org[0:c,i:i+r]
#     cv2.imwrite(str(i)+'.jpg',res)
org=cv2.cvtColor(org,cv2.COLOR_RGB2GRAY)
(r,c)=org.shape
res=np.zeros((r,c),dtype='uint8')
flag=False
for i in range(c):
    if org[r-35,i]<240 and flag==False:
        x1=i
        flag=True
    elif org[r-35,i]>240 and flag==True:
        x2=i
        res=org[0:r,x1:x2]
        cv2.imwrite(str(i)+'.jpg',res)
        flag=False





