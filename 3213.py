from selenium import webdriver
import unittest
import time

class TestAbs(unittest.TestCase):
    def tests(self):
        
        def test_form(url):
            browser = webdriver.Chrome()
            browser.get(url)
            browser.find_element_by_css_selector(".first_block .first_class input").send_keys("Ivan")
            browser.find_element_by_css_selector(".first_block .second_class input").send_keys("Petrov")
            browser.find_element_by_css_selector(".first_block .third_class input").send_keys("qwe@gmail.com")

            browser.find_element_by_xpath("//button[text()[contains(.,'Submit')]]").click()
            time.sleep(3)
            welcome = browser.find_element_by_tag_name("h1").text
            self.assertEqual(u"Congratulations! You have successfully registered!", welcome)

        test_form("http://suninjuly.github.io/registration1.html")
        test_form("http://suninjuly.github.io/registration2.html")


if __name__ == "__main__": 
        unittest.main()