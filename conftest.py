import pytest
from selenium import webdriver


# обработчик, который считывает из командной строки параметры browser_name и language
# а потом в getoption его значение присваиваем browser_name и language
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or en")


@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        
        options_chrome = webdriver.ChromeOptions()
        options_chrome.add_experimental_option('excludeSwitches', ['enable-logging'])
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': user_language})   # объявление нужного языка

        #options_chrome.add_argument('--start-maximized')        # развернуть окно на весь экран
        
        browser = webdriver.Chrome(options=options_chrome)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        
        options_firefox = webdriver.FirefoxOptions()
        options_firefox.set_preference("intl.accept_languages", user_language)     # объявление нужного языка

        browser = webdriver.Firefox(options=options_firefox)
    
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox and --language should be ru or en")
    
    yield browser
    print("\nquit browser..")
    browser.quit()