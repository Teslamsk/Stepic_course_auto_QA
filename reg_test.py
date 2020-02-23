import unittest
import time
from selenium import webdriver

# Данный код - иллюстрация моих навыков в написании автотестов для формы регистрации.
# Имеются две ссылки, одна рабочая, в другой - верстальщик пропустил одно обязательное поле.

# В коде реализованы три сценария:
# - Заполяем все поля, ожидаем, что форма сработает;
# - Заполняем только обязательные поля, ожидаем, что форма сработает;
# - Заполняем только не обязательные поля, ожидаем, что форма не сработает.

# Форма для тестирования рабочая:
link = "http://suninjuly.github.io/registration1.html"

# Форма для тестирования с ошибкой - пропущено обязательное поле:
# link = "http://suninjuly.github.io/registration2.html"


class TestRegistration(unittest.TestCase):
    def test_all_fields(self):

        try:
            browser = webdriver.Chrome()
            browser.get(link)
            browser.implicitly_wait(5)

            # Проверка обязательных для заполнения полей
            input1 = browser.find_element_by_css_selector('div .first_block div .first')
            input1.send_keys("Vasiliy")
            input2 = browser.find_element_by_css_selector('div .first_block div .second')
            input2.send_keys("Pupkin")
            input3 = browser.find_element_by_css_selector('div .first_block div .third')
            input3.send_keys("test@gmail.com")
            # Проверка необязательных полей
            input4 = browser.find_element_by_css_selector('div .second_block div .first')
            input4.send_keys("+79151234567")
            input2 = browser.find_element_by_css_selector('div .second_block div .second')
            input2.send_keys("Russia, Jmerinka")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                             "Registration form error! It doesn't work!")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_required_fields(self):

        try:
            browser = webdriver.Chrome()
            browser.get(link)
            browser.implicitly_wait(5)

            # Проверка обязательных для заполнения полей
            input1 = browser.find_element_by_css_selector('div .first_block div .first')
            input1.send_keys("Vasiliy")
            input2 = browser.find_element_by_css_selector('div .first_block div .second')
            input2.send_keys("Pupkin")
            input3 = browser.find_element_by_css_selector('div .first_block div .third')
            input3.send_keys("test@gmail.com")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                             "Registration form error! It doesn't work!")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_unnecessary_fields(self):
        try:
            browser = webdriver.Chrome()
            browser.get(link)
            browser.implicitly_wait(5)

            # Проверка необязательных полей
            input4 = browser.find_element_by_css_selector('div .second_block div .first')
            input4.send_keys("+79151234567")
            input2 = browser.find_element_by_css_selector('div .second_block div .second')
            input2.send_keys("Russia, Jmerinka")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertNotEqual("Congratulations! You have successfully registered!", welcome_text,
                                "Registration form error! It mustn't work but it does!")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()
