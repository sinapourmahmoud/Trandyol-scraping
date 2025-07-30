from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Trandyol(webdriver.Firefox):
    items=[]
    def __init__(self):
        super().__init__()
    
    def get_items(self,product,url,limit=1):
        count=1
        
        while count<=limit:
            
            
            try:
                self.get(f'{url}?pi={count}')
                category=self.find_element(By.CSS_SELECTOR,'.dscrptn h1').text
                roots=self.find_elements(By.CSS_SELECTOR,'.p-card-chldrn-cntnr.card-border')
                for root in roots:
                    item={}
                    item['company']=root.find_element(By.CSS_SELECTOR,'.prdct-desc-cntnr-ttl').text
                    item['link']='https://www.trendyol.com'+root.get_attribute("href")
                    item['category']=category
                    item['product']=product
                    item['name']=root.find_element(By.CSS_SELECTOR,'.prdct-desc-cntnr-name').text
                    item['rate']=float(root.find_element(By.CSS_SELECTOR,'.rating-score').text)
                    item['price']=float(root.find_element(By.CSS_SELECTOR,'.price-item').text[:root.find_element(By.CSS_SELECTOR,'.price-item').text.find('T')-1].replace(",","."))
                    Trandyol.items.append(item)
                
            
            except:
                ...
            count+=1