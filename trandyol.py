from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
class Trandyol(webdriver.Firefox):
    items=[]
    def __init__(self):
        super().__init__()
    
    def get_items(self,product,url,limit=20):
        count=1
        
        while count<=limit:
            
            
            try:
                self.get(f'{url}?pi={count}')
                category=self.find_element(By.CSS_SELECTOR,'.dscrptn h1').text
                roots=self.find_elements(By.CSS_SELECTOR,'.p-card-chldrn-cntnr.card-border')
                for root in roots:
                    item=[]
                    item.append(root.find_element(By.CSS_SELECTOR,'.prdct-desc-cntnr-name').text or "")
                    item.append(root.find_element(By.CSS_SELECTOR,'.prdct-desc-cntnr-ttl').text or "")
                    item.append(root.get_attribute("href") or "")
                    item.append(float(root.find_element(By.CSS_SELECTOR, '.rating-score').text or "0"))
                    item.append(product or "")
                    item.append(category or "")
                    item.append(float(root.find_element(By.CSS_SELECTOR,'.price-item').text[:root.find_element(By.CSS_SELECTOR,'.price-item').text.find('T')-1].replace(",",".") or "0"))
                    Trandyol.items.append(item)

            except:
                ...
            count+=1


def get_item(url):
        firefox_options = Options()
        firefox_options.headless = True
        web_driver=webdriver.Firefox(options=firefox_options)
        attribute_items=[]



        web_driver.get(url)
        product_title = web_driver.find_element(By.CSS_SELECTOR, '.product-title').text
        price = web_driver.find_element(By.CSS_SELECTOR, '.discounted').text
        items = web_driver.find_elements(By.CSS_SELECTOR, '.attribute-item')
        lis = web_driver.find_elements(By.CSS_SELECTOR, '.content-description-item-description')
        options = []
        for li in lis:
            options.append(li.text)
        for item in items:
            attribute_items.append({"name": item.find_element(By.CSS_SELECTOR, '.name').text,
                                    'value': item.find_element(By.CSS_SELECTOR, '.value').text})
        return {'title': product_title , 'price': price, 'attribute_items': attribute_items,
                'options': options}


