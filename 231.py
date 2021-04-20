import os 
import math
from selenium import webdriver
link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector('button').click()
browser.switch_to.alert.accept()
x = int(browser.find_element_by_xpath("//*[@id='input_value']").text)

browser.find_element_by_xpath("//*[@id='answer']").send_keys(str(math.log(abs(12*math.sin(x)))))
browser.find_element_by_xpath("//button[text()[contains(.,'Submit')]]").click()