from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os


options = Options()
#options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")

filename = "C:\\Users\\hewbo\\AppData\\Local\\Programs\\Python\\chromedriver.exe"


browser = webdriver.Chrome(options=options, executable_path=filename)

browser.get("https://tinder.com/app/recs")


time.sleep(50)


like = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]")


while(True):
	like.click()

