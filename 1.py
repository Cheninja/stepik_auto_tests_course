from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x1 = browser.find_element_by_id('num1').text
    x2 = browser.find_element_by_id('num2').text
    sum = int(int(x1)+int(x2))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text('%s'  % sum)
    tap = browser.find_element_by_class_name('btn-default').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла