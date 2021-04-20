from selenium import webdriver
link = "http://suninjuly.github.io/get_attribute.html"
import math

browser = webdriver.Chrome()
browser.get(link)

x = int(browser.find_element_by_xpath("//*[@id='treasure']").get_attribute('valuex'))

browser.find_element_by_xpath("//*[@id='answer']").send_keys(str(math.log(abs(12*math.sin(x)))))
browser.find_element_by_xpath("//*[@id='robotCheckbox']").click()
browser.find_element_by_xpath("//*[@id='robotsRule']").click()
button = browser.find_element_by_xpath("//button[text()[contains(.,'Submit')]]")
button.click()
