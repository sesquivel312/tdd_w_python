from selenium import webdriver

browser = webdriver.Chrome('/home/steve/bin/chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title