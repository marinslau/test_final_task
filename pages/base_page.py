class BasePage():

    # конструктор — метод, который вызывается, когда мы создаем объект
	def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # метод открывает нужную страницу, используя метод get()
    def open(self):
    	self.browser.get(self.url)