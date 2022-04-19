from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id('input_value').text
    y = calc(int(x))
    input = browser.find_element_by_class_name('form-control')
    input.send_keys(y)
    browser.execute_script("window.scrollBy(0, 140);")
    check = browser.find_element_by_id('robotCheckbox').click()
    robot = browser.find_element_by_id('robotsRule').click()
    button = browser.find_element_by_class_name('btn-primary').click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла