import os 
from selenium import webdriver
link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

browser.find_element_by_css_selector('[name = "firstname"]').send_keys("Иван")
browser.find_element_by_css_selector('[name = "lastname"]').send_keys("Петров")
browser.find_element_by_css_selector('[name = "email"]').send_keys("petrov@mail.ru")
browser.find_element_by_css_selector('[type = "file"]').send_keys(file_path)
browser.find_element_by_xpath("//button[text()[contains(.,'Submit')]]").click()
