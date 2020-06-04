from selenium.webdriver.common.by import By

class WebContainer:
    def __init__(self, context):
        self.context = context

    def f(self, id, by = By.XPATH):
        return self.context.find_element(by, id)

    def ff(self, id, by = By.XPATH):
        return self.context.find_elements(by, id)
