import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

link = 'http://suninjuly.github.io/explicit_wait2.html'

# код для математической функции
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector('#book')
    price = WebDriverWait(browser, 200).until(ec.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()
    time.sleep(1)
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    # Посчитать математическую функцию.
    y = calc(x)
    # Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(str(y))
    input4 = browser.find_element_by_css_selector('#solve')
    input4.click()

    time.sleep(5)

finally:
    time.sleep(5)
    browser.quit()

