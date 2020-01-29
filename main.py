# Jasar Orion Cirelli - jasaroc@gmail.com
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib
import argparse
import urllib2
import time

searchterm = raw_input("Termos de busca => ")
url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
browser = webdriver.Chrome()
browser.get(url)
counter = 0
succounter = 0

DIR= searchterm
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
if not os.path.exists(searchterm):
    os.mkdir(searchterm)

for _ in range(5000):
    browser.execute_script("window.scrollBy(0,1000000)")

for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
    counter = counter + 1
    img = json.loads(x.get_attribute('innerHTML'))["ou"]    
    image_type = json.loads(x.get_attribute('innerHTML'))["ity"]

    try:
        req = urllib2.Request(img, headers={'User-Agent' : header})
        raw_img = urllib2.urlopen(req).read()

        cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
        print cntr
        if len(image_type)==0:
            f = open(os.path.join(DIR , str(time.time()) + ".jpg"), 'wb')
        else :
            f = open(os.path.join(DIR , str(time.time()) + "." +image_type), 'wb')


        f.write(raw_img)
        f.close()
    except Exception as e:
        print "could not load : "+img
        print e

print(succounter, "pictures succesfully downloaded")
browser.close()