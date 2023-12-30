from .base_page import BasePage
from .locators import BasketPageLocators



class BasketPage(BasePage):

	# при переходе с главной - корзина пустая
	def should_be_empty_basket_page(self):
		self.should_not_be_any_product_in_basket()
		self.should_be_text_empty_basket()


	# продукты в корзине отсутствуют - негативная проверка
	def should_not_be_any_product_in_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET_TITLE), "Basket isn't empty"

	# текст о пустой корзине присутствует
	def should_be_text_empty_basket(self):
		assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Text about empty basket doesn't exist"