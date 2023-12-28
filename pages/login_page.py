from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url, "Url does not contain 'login'"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"



# для тестов @pytest.mark.authorized_user
    def register_new_user(self, email, password):

        email_area = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_area.send_keys(email)

        password_area = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_area.send_keys(password)

        password_area_again = self.browser.find_element(*LoginPageLocators.PASSWORD_AGAIN)
        password_area_again.send_keys(password)

        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()