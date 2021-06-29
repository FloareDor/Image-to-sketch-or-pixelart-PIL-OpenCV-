import cv2
import time
from PIL import Image
#img_location = input("Please input your image location: ")
img_location = 'C:/Users/GAGVAP/Downloads/Pixel Art/Project_B/'
fileName = input("Please input your image name: ")
command = input('''Please input the conversion style: 
1)"pencil" for pencil sketch
2)"pixel" for pixel art
: ''').lower()

if "pencil" in command and "pixel" not in command:
    img = cv2.imread(img_location+fileName)
    #cv2.imshow('original_Img', img)
    #cv2.imshow('Original Image', img)
    gray_Img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_img = 255 - gray_Img
    blurred_Img = cv2.GaussianBlur(inverted_img, (27,27), 0)
    inv_blurred_Img = 255 - blurred_Img
    pencil_Sketch_Img = cv2.divide(gray_Img, inv_blurred_Img, scale = 256.0)
    cv2.imshow('pencil_Sketch', pencil_Sketch_Img)
    #pencil_Sketch_Img.save('conv_Result.jpg')
    cv2.waitKey(0)
elif "pixel" in command and "pencil" not in command:
    myImage = Image.open(img_location+fileName)
    smolImage = myImage.resize((88, 88), Image.BILINEAR)
    result = smolImage.resize(myImage.size, Image.NEAREST)
    result.save('conv_Result.png')





