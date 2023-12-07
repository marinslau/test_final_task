class BasePage():

    # конструктор — метод, который вызывается, когда мы создаем объект
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)