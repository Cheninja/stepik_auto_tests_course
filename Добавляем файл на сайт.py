from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector("[name = 'firstname']")
    input1.send_keys("О Да")
    input2 = browser.find_element_by_css_selector("[name = 'lastname']")
    input2.send_keys("Окей")
    input3 = browser.find_element_by_css_selector("[name = 'email']")
    input3.send_keys("@mail")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element = browser.find_element_by_id('file')
    element.send_keys(file_path)

    button = browser.find_element_by_class_name('btn-primary').click()




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла