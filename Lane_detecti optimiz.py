import cv2
import matplotlib.pyplot as plt
import numpy as np

def resized(image,scale_factor):
    scale_percent = scale_factor
    img=image
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    result=cv2.resize(img,(width,height),interpolation = cv2.INTER_AREA)
    return result 

def canny(image):        
    gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur_img=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur_img,100,150)
    return canny
def region_of_intrest(image):
    polygon=np.array([[(0,600),(190,110),(480,110),(image.shape[1],600)]])
    mask=np.zeros_like(image)
    mask=cv2.fillPoly(mask,polygon,255)
    masked_img=cv2.bitwise_and(image,mask)
    return masked_img 

def find_lines(lines,image):
     left_lines=[]
     right_lines=[]
     for line in lines:
         x1,y1,x2,y2=line.reshape(4)
         parameters=np.polyfit((x1,x2),(y1,y2),1)
         slope=parameters[0]
         y_intercept=parameters[1]
         if slope<0:
             left_lines.append((slope,y_intercept))
         else:
             right_lines.append((slope,y_intercept))
     average_left=np.average(left_lines,axis=0)
     average_right=np.average(right_lines,axis=0)
     return (average_left,average_right,image)
def displaylines(combo):
    
    left_line=combo[0]
    right_line=combo[1]
    img= combo[2]
    y1=img.shape[0]
    y2=int(y1*(1/5))
    x1=int((y1-left_line[1])/left_line[0])
    x2=int((y2-left_line[1])/left_line[0])
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),10)
    y1=img.shape[0]
    y2=int(y1*(1/5))
    x1=int((y1-right_line[1])/right_line[0])
    x2=int((y2-right_line[1])/right_line[0])
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),10)
    
    return img

cap=cv2.VideoCapture('D:\\codes\\Car lane detection\\test.mp4')
while(cap.isOpened()):
    _,frame=cap.read()
    canny_img=canny(frame)
    cropped_img=region_of_intrest(canny_img)
    lines=cv2.HoughLinesP(cropped_img,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5 )
    combo=find_lines(lines,frame)
    line_img=displaylines(combo)
    
    
    cv2.imshow('output',line_img)
    cv2.waitKey(1)


    