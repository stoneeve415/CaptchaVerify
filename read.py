# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np
import glob

number = ['0','1','2','3','4','5','6','7','8','9']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
global txt_filenames
txt_filenames = []
# i = 0
def get_img_and_text(i):
      global txt_filenames
      print 'start'
      if len(txt_filenames) == 0:
            txt_filenames = glob.glob('img/*.jpg')
      text = txt_filenames[i]
      captcha_text = text[4:8]
      captcha_image = Image.open(txt_filenames[i])
      captcha_image = np.array(captcha_image)
      # i = i + 1
      return captcha_text, captcha_image

if __name__ == '__main__':
      for i in range(0,800):
            text, image = get_img_and_text(i)
            print i
            print text
