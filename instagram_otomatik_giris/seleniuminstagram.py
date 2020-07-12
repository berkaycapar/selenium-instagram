from selenium import webdriver #webdriver dahil ediliyor
import time

browser = webdriver.Firefox()
browser.get("https://www.instagram.com")
time.sleep(5)
#giris_yap=browser.find_element_by_xpath("")
username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")
username.send_keys("ur username")
password.send_keys("ur password")
login = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]/button")
login.click()
time.sleep(10)
browser.close()
