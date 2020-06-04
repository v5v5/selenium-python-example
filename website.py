from webcontainer import WebContainer
from page_tesla import PageTesla

class WebSite(WebContainer):
    def __init__(self, context):
        self.page_tesla = PageTesla(context)