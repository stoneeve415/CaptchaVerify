# -*- coding: utf-8 -*-
import time
import urllib
import os
from splinter import Browser
from PIL import Image
from handle import *
from splinter.driver.webdriver.remote import WebDriver
def downloadImage(imageUrl,text):
    path = "pic/"+text+".jpg"
    data = urllib.urlopen(imageUrl).read()  
    f = file(path,"wb")  
    f.write(data)  
    f.close()
    fixed_size(path, 160, 60)
  
def splinter(url,url2,url3):
    remote_server_url ="http://127.0.0.1:4444/wd/hub"
    # remote_server_url="http://123.207.227.64/"
    text = 'text'
    with Browser(driver_name="remote",
                 url=remote_server_url,
                 browser='firefox',
                ) as browser:
        browser.visit(url)
        browser.find_by_id('userNameLogin').fill('luwind')
        browser.find_by_id('pwd').fill('s1o2n3567')
        browser.find_by_id('loginFlagnew').click()
        browser.find_by_id('pwd').fill('s1o2n3567')
        # time.sleep(2)
        for i in range(100):
            browser.find_by_id('pwd').fill('s1o2n3567')
            imgurl = browser.find_by_id('validateImg')['src']
            # get current image
            downloadImage(imgurl, 'current')
            # resize the current img and get its gray
            fixed_size("pic/current.jpg", 160, 60)
            # judge
            # text = getText()

            browser.find_by_id('validNum').fill(text)

            # time.sleep(1)
            # browser.find_by_id('loginFlagnew').click()
            if browser.is_text_present(u'验证码错误。'):
                print 'failed'
            else:
                print 'succeed'
                downloadImage(imgurl, text)
                browser.find_by_id('pwd').fill('s1o2n3567')
                browser.find_by_id('validNum').fill(text)


    # text='text'
    # browser = Browser(driver_name="firefox")
    # browser.visit(url)
    # browser.find_by_id('userNameLogin').fill('luwind')
    # browser.find_by_id('pwd').fill('s1o2n3567')
    # browser.find_by_id('loginFlagnew').click()
    # browser.find_by_id('pwd').fill('s1o2n3567')
    # # time.sleep(2)
    # for i in range(100):
    #     browser.find_by_id('pwd').fill('s1o2n3567')
    #     imgurl = browser.find_by_id('validateImg')['src']
    #     #get current image
    #     downloadImage(imgurl, 'current')
    #     #resize the current img and get its gray
    #     fixed_size("pic/current.jpg",160, 60)
    #     #judge
    #     #text = getText()
    #
    #     browser.find_by_id('validNum').fill(text)
    #
    #     # time.sleep(1)
    #     # browser.find_by_id('loginFlagnew').click()
    #     if browser.is_text_present(u'验证码错误。'):
    #         print 'failed'
    #     else:
    #         print 'succeed'
    #         downloadImage(imgurl, text)
    #         browser.find_by_id('pwd').fill('s1o2n3567')
    #         browser.find_by_id('validNum').fill(text)
    

if __name__ == '__main__':
    website1 ='https://user.lu.com/user/login?returnPostURL=https%3A%2F%2Flist.lu.com%2Flist%2Fbianxiantong'
    website3 ='https://list.lu.com/list/bianxiantong'
    website2 ='https://lumi.lu.com/lumi/index'
    splinter(website1,website2,website3)
