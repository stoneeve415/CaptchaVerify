#-*- coding:utf-8 -*-
from PIL import Image
from kmeans import *
import glob
# 把彩色图像转为灰度图像（色彩对识别验证码没有什么用）
def convert2gray(img):
    if len(img.shape) > 2:
        gray = np.mean(img, -1)
        # 上面的转法较快，正规转法如下
        # r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
        # gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return gray
    else:
        return img

def fixed_size(filename,width, height):
    """按照固定尺寸处理图片"""
    out_filename = filename
    print out_filename
    im = array(Image.open(filename))
    h = im.shape[0]
    w = im.shape[1]
    codeim = clusterpixels_rectangular(filename, m_k, getfirststeps(im, m_maxsteps))
    for i in range(h):
        for j in range(w):
            if (codeim[i * w + j] == codeim[0]):
                im[i][j] = [255, 255, 255]
            else:
                im[i][j] = im[i][j]
    cv2.imwrite(out_filename,im)
    im = Image.open(out_filename)
    out = im.resize((width, height), Image.ANTIALIAS)
    out.save(out_filename)