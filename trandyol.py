from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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