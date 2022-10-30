import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
import urllib.request
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://www.google.co.kr/imghp?hl=ko'

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=5)
search_box = driver.find_element_by_class_name('gLFyf')

flag = True
a=[]

while flag == True:
    input_fish = input("물고기 이름을 입력하세요(빈칸입력시종료): ")
    if input_fish == "":
        flag = False
    else:
        a.append(input_fish)

for index , value in enumerate(a):
    print(value)
    os.mkdir(value)
    search_box = driver.find_element_by_class_name('gLFyf')
    time.sleep(2)
    
    search_box.send_keys(value)
    search_box.send_keys(Keys.ENTER)

    images = driver.find_elements_by_class_name("rg_i.Q4LuWd")
    
    i = 1
    for image in images:
        image.click()
        down_url = driver.find_element(By.CSS_SELECTOR, ".n3VNCb").get_attribute("src")
        urllib.request.urlretrieve(down_url, f"{value}/{value} {i}번.jpg")
        i += 1
        if i == 301:
            break
    URL = 'https://www.google.co.kr/imghp?hl=ko'
    driver.get(URL)
