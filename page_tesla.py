from webcontainer import WebContainer
from panel_example import PanelExample

class PageTesla(WebContainer):
    url = "https://finance.yahoo.com/quote/TSLA/financials?p=TSLA"

    @property
    def text_revenue(self):
        return self.f('//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/span')
        
    @property
    def text_cost_of_revenue(self):
        return self.f('//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/span')

    @property
    def text_gross_profit(self):
        return self.f('//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/div[1]/div[2]/div[3]/div[1]/div[3]/span')
    
    @property
    def panel_example(self):
        return PanelExample(self.f('//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/div[1]/div[2]'))

