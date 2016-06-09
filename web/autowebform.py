import time
from selenium import webdriver

chrome = webdriver.Chrome('./chromedriver')

# 네이버 홈페이지 로그인 양식 작성
chrome.get('http://www.naver.com')
form_id = chrome.find_element_by_id('id')
form_pw = chrome.find_element_by_id('pw')

form_id.send_keys('no-such-user')
form_pw.send_keys('1234')
time.sleep(5)

chrome.quit()
