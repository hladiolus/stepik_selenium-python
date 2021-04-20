from selenium import webdriver
link = "https://suninjuly.github.io/execute_script.html"
import math

browser = webdriver.Chrome()
browser.get(link)

x = int(browser.find_element_by_xpath("//*[@id='input_value']").text)

browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element_by_xpath("//*[@id='input_value']"))

browser.find_element_by_xpath("//*[@id='answer']").send_keys(str(math.log(abs(12*math.sin(x)))))
browser.find_element_by_xpath("//*[@for='robotCheckbox']").click()
browser.find_element_by_xpath("//*[@for='robotsRule']").click()
button = browser.find_element_by_xpath("//button[text()[contains(.,'Submit')]]")
button.click()
