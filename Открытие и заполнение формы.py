from selenium import webdriver
import time
i = 0
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        if i == 0:
            element.send_keys("Серега")
            i += 1
        elif i == 1:
            element.send_keys("Да")
            i += 1
        elif i%2==0:
            element.send_keys("Мой ответ")
            i += 1
        else:
            element.send_keys("Не мой ответ")
            i+=1

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла