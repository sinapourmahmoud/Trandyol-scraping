from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
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



def create_headless_firefox():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--width=1920')
    options.add_argument('--height=1080')

    service = Service(executable_path=GeckoDriverManager().install())

    driver = webdriver.Firefox(service=service, options=options)
    return driver

def get_item(url):
        web_driver=create_headless_firefox()
        attribute_items=[]



        web_driver.get(url)
        try:
            product_title = web_driver.find_element(By.CSS_SELECTOR, '.product-title').text
        except:
            product_title='not found'
        try:
            price = web_driver.find_element(By.CSS_SELECTOR, '.discounted').text
        except:
            price='not found'
        try:
            items = web_driver.find_elements(By.CSS_SELECTOR, '.attribute-item')
        except:
            items = 'no atribute items found'

        try:
            lis = web_driver.find_elements(By.CSS_SELECTOR, '.content-description-item-description')
        except:
            lis = 'no description found'


        options = []
        for li in lis:
            options.append(li.text)
        try:
            for item in items:
                attribute_items.append({"name": item.find_element(By.CSS_SELECTOR, '.name').text,
                                        'value': item.find_element(By.CSS_SELECTOR, '.value').text})
        except:
            attribute_items = []
        return {'title': product_title , 'price': price, 'attribute_items': attribute_items,
                'options': options}



