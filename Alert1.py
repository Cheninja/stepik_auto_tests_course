from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    but1 = browser.find_element_by_class_name("btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id('input_value').text
    y = calc(int(x))
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    but1 = browser.find_element_by_class_name("btn-primary").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()