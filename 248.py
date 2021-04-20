import os 
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

wait = WebDriverWait(browser, 12)
element = wait.until(EC.text_to_be_present_in_element((By.ID,'price'), '$100'))

browser.find_element_by_css_selector('button').click()

x = int(browser.find_element_by_xpath("//*[@id='input_value']").text)

browser.find_element_by_xpath("//*[@id='answer']").send_keys(str(math.log(abs(12*math.sin(x)))))
browser.find_element_by_xpath("//button[text()[contains(.,'Submit')]]").click()