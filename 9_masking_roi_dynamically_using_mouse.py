import cv2
import numpy
from copy import deepcopy as dp

start_row=0
end_row=1
start_col=0
end_col=1
flag=0
mask=0
select_flag=0
a=0
def masked(event,x,y,flags,param):
    global a,start_row,start_col,end_row,end_col,flag,mask,select_flag,img
    if event==cv2.EVENT_LBUTTONDOWN:
        start_row=y
        start_col=x
        select_flag=1
    if event==cv2.EVENT_MOUSEMOVE:
        if select_flag==1:
            end_row=y+1
            end_col=x+1
            min_row=min(start_row,end_row)
            max_row=max(start_row,end_row)
            min_col=min(start_col,end_col)
            max_col=max(start_col,end_col)
            mask=tmg[min_row:max_row,min_col:max_col]
            b=(str(min_row)+':'+str(max_row)+','+str(min_col)+':'+str(max_col))
            if a!=b:
                a=b
            flag=1
            cv2.rectangle(img,(start_col,start_row),(end_col-1,end_row-1),(0,0,255),-1)
    if event==cv2.EVENT_LBUTTONUP:
        flag=0
        select_flag=0
        img=dp(tmg)
        
path='a.jpg'  #provide_image_path
img=cv2.imread(path,1)
tmg=dp(img)
cv2.namedWindow('image')
cv2.namedWindow('mask')
cv2.setMouseCallback('image',masked)
while True:
    cv2.imshow('image',img)
    if flag==1:
        try:
            cv2.imshow('mask',mask)
        except cv2.error:
            pass
    if cv2.waitKey(1)==27:
        break
cv2.destroyWindow('image')
print(a)  #you will get the mask 
