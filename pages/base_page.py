from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import math

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators


class BasePage():

    # конструктор — метод, который вызывается, когда мы создаем объект
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)     # неявное ожидание, автоматически при поиске элементов

    def open(self):
        self.browser.get(self.url)

    

    # метод, который проверяет существует ли элемент
    def is_element_present(self, method, css_selector):
        try:
            self.browser.find_element(method, css_selector)
        except NoSuchElementException:
            return False
        return True

    # негативная проверка
    # метод, который проверяет, что элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, method, css_selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((method, css_selector)))
        except TimeoutException:
            return True
        return False

    # негативная проверка
    # метод, который проверяет, что какой-то элемент исчезает
    # 1 - означает частоту опроса - т.е. WebDriver ждёт 4 секунды и делает запросы каждую секунду
    def is_disappeared(self, method, css_selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((method, css_selector)))
        except TimeoutException:
            return False
        return True



    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basket_page(self):
        basket_button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket_button.click()



    # алерт - проверочный код
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")