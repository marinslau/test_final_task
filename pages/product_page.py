from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

	def add_product_to_basket(self):
		add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
		add_button.click()



	# проверка сообщений после добавления товара
	def should_be_message_page(self):
		self.should_be_message_add_product()
		self.should_be_message_price_product()

	# Проверка того, что товар добавлен в корзину. 
	# Название товара в сообщении должно совпадать с тем товаром, который добавили
	def should_be_message_add_product(self):
		assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_NAME), "Message about add product doesn't exist"
		
		product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
		#print(product_name, message_product_name)
		assert message_product_name == product_name, "The product's name in the message doesn't match product's name on the page"
		
	# Проверка стоимости в корзине. Стоимость в корзине должна совпадать с ценой товара
	def should_be_message_price_product(self):
		assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_PRICE), "Message about product's price doesn't exist"
		
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		message_product_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE).text
		#print(product_price, message_product_price)
		assert message_product_price == product_price, "The product's price in the message doesn't match product's price on the page"



	# проверка, что нет сообщения об успешном добавлении продукта
	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

	# проверка после добавления в корзину, что сообщение о добавлении товара исчезает
	def success_message_should_disappear(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappear, but should be"