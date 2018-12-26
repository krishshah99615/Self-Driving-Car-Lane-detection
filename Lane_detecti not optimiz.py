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
def Display_lines(image,lines):
    
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2= line.reshape(4)
            cv2.line(image,(x1,y1),(x2,y2),(255,0,0),10)
        return image    
img=cv2.imread('D:\\codes\\Car lane detection\\lane_img.jpg')
img=resized(img,20)
img=np.copy(img)




cap=cv2.VideoCapture('D:\\codes\\Car lane detection\\test.mp4')
while(cap.isOpened()):
    _,frame=cap.read()
    canny_img=canny(frame)
    cropped_img=region_of_intrest(canny_img)
    lines=cv2.HoughLinesP(cropped_img,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5 )
    line_img=Display_lines(frame,lines)
    
    cv2.imshow('output',line_img)
    cv2.waitKey(1)    

     