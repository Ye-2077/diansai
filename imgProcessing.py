import cv2
import numpy as np


def cv2show(figure:str, img):
    '''show the image by cv2'''
    
    cv2.imshow(figure,img)
    cv2.waitKey(0) # press 0 to stop showing 
    cv2.destroyAllWindows()


def addNoise(s_vs_p:float, amount:float, img, path:str):
    '''
    add salt and pepper noise to image
        - s_vs_p: the proportion of salt noise
        - amount: the amount of noise
        - img: the target
    '''
    
    noise_img = np.copy(img)
    
    # add salt(white) noise
    salt_num = np.ceil(amount * img.size * s_vs_p)
    # set the salt location of noise
    salt_coords = [np.random.randint(0,i - 1, int(salt_num)) for i in img.shape]
    noise_img[salt_coords[0],salt_coords[1],:] = [255,255,255]
    
    # add pepper(black) noise
    num_pepper = np.ceil(amount * img.size * (1. - s_vs_p))
    # set the pepper location of noise
    pepper_coords = [np.random.randint(0,i - 1, int(num_pepper)) for i in img.shape]
    noise_img[pepper_coords[0],pepper_coords[1],:] = [0,0,0]
    
    cv2.imwrite(path,noise_img)

    
def  gaussian_blur(img):
    '''Perform Gaussian filtering'''
    
    gaussian_img = cv2.GaussianBlur(img,(5,5),10)
    return gaussian_img


def im2bw(img, Auto='on', thresh=0):
    '''change the image to black and white stlye'''
    
    if Auto == 'on':
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
        img_bw = cv2.threshold(img_grey, 0, 255, cv2.THRESH_OTSU+cv2.THRESH_BINARY)[1]
    elif Auto == 'off':
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
        img_bw = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]
    return img_bw


# 形态学处理
def morphThreat(img, dilate_num, erode_num, kernel_size):
    '''形态学处理'''
    
    kernel = np.ones((kernel_size,kernel_size),np.uint8)
    # 膨胀
    cv2.dilate(img,kernel, dilate_num)
    # 腐蚀
    cv2.erode(img, kernel, erode_num)
    
    return img

# 提取轮廓
def GetContours(img):
    '''提取轮廓'''
    
    global contours
    # 根据二值图找到轮廓
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
 
    # 画出轮廓
    dst = img.copy()
    dst = cv2.cvtColor(dst,cv2.COLOR_GRAY2RGB)
    dst = cv2.drawContours(dst, contours, -1, (0, 0, 255),3)
    return dst



