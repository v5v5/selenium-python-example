from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from website import WebSite

driver = None
try:
    driver = webdriver.Chrome("C:/chromedriver.exe")
    website = WebSite(driver)

    driver.get(website.page_tesla.url)
    print(driver.title)

    # print(page.text_revenue.text)
    # print(page.text_cost_of_revenue.text)
    # print(page.text_gross_profit.text)

    print(website.page_tesla.panel_example.text_revenue.text)
    print(website.page_tesla.panel_example.text_cost_of_revenue.text)
    print(website.page_tesla.panel_example.text_gross_profit.text)

finally:
    if driver is not None:
        print("webdriver closing...")
        driver.quit()
        print("webdriver closed.")
