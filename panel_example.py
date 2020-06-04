from webcontainer import WebContainer

class PanelExample(WebContainer):

    @property
    def text_revenue(self):
        return self.f('./div[1]/div[1]/div[3]/span')
        
    @property
    def text_cost_of_revenue(self):
        return self.f('./div[2]/div[1]/div[3]/span')

    @property
    def text_gross_profit(self):
        return self.f('./div[3]/div[1]/div[3]/span')


