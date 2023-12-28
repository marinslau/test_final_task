from .pages.product_page import ProductPage

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

import pytest

# для тестов @pytest.mark.authorized_user
import time


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.add_product_to_basket()
	product_page.solve_quiz_and_get_code()
	product_page.should_be_message_page()        # проверка сообщений после добавления товара


# предыдущий тест, переписанный с параметризацией
@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="fixing this bug right now")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket_offer0_offer9(browser, link):
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.add_product_to_basket()
	product_page.solve_quiz_and_get_code()
	product_page.should_be_message_page()        # проверка сообщений после добавления товара


@pytest.mark.skip
@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.add_product_to_basket()
	product_page.should_not_be_success_message()        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
 

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.should_not_be_success_message()      # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


@pytest.mark.skip
@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.add_product_to_basket()
	product_page.success_message_should_disappear()     # Проверяем, что сообщение об успехе исчезает с помощью is_disappeared


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()
	login_page = LoginPage(browser, browser.current_url)   # инициализируем LoginPage
	login_page.should_be_login_page()
	

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_basket_page()                                 
	basket_page = BasketPage(browser, browser.current_url)   # инициализируем BasketPage
	basket_page.should_be_empty_basket_page()



# ДЛЯ УЧЕБНЫХ ЦЕЛЕЙ 
# т.к реализовать можно с помощью API или напрямую через базу данных
@pytest.mark.authorized_user
class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):                                              # действия, производимые до каждого теста в классе
		link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
		email = str(time.time()) + "@fakemail.org"                         # генерируем рандомный email
		password = "amzpassword"                                           # рандомный пароль
		login_page = LoginPage(browser, link)
		login_page.open()
		login_page.register_new_user(email=email, password=password)       # передаем email и password в register_new_user
		login_page.should_be_authorized_user()

	def test_user_cant_see_success_message(self, browser):                             
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
		product_page = ProductPage(browser, link)
		product_page.open()
		product_page.should_not_be_success_message()

	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
		product_page = ProductPage(browser, link)
		product_page.open()
		product_page.add_product_to_basket()
		product_page.should_be_message_page()