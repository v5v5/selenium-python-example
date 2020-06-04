from selenium.webdriver.remote.webelement import WebElement

class Element(WebElement):
    def __init__(self, context, by, id):
        self.context = context
        self.by = by
        self.id = id

    def __call__(self):
        return self.context.find_element(self.by, self.id)
