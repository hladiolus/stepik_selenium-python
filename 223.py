from selenium import webdriver
link = "http://suninjuly.github.io/selects1.html"
import math

browser = webdriver.Chrome()
browser.get(link)

x = int(browser.find_element_by_xpath("//*[@id='num1']").text) + int(browser.find_element_by_xpath("//*[@id='num2']").text)

browser.find_element_by_xpath("//*[@id='dropdown']").click()
browser.find_element_by_xpath("//*[@value='" + str(x) + "']").click()
button = browser.find_element_by_xpath("//button[text()[contains(.,'Submit')]]")
button.click()