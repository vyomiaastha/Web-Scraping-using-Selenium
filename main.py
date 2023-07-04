from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

browser = webdriver.Chrome()

books_dic=[]
load_more = True;

url = 'https://www.bookswagon.com/promo-best-seller/best-seller/03AC998EBDC2?sid=407452'
browser.get(url)


while load_more:
    
    try:
        items = browser.find_elements(By.CSS_SELECTOR,'.row.bestsellerbox .card.align-items-center')


        if items:
            for item in items:
                title = item.find_element(By.CSS_SELECTOR,'span.booktitle.font-weight-bold').text
                author = item.find_element(By.CSS_SELECTOR,'.author.authortextcolor').text
                price = item.find_element(By.CSS_SELECTOR,'.actualprice.themecolor.font-weight-bold').text
                link = item.find_element(By.CSS_SELECTOR,'.card.align-items-center a').get_attribute('href')
                
                books_dic.append({

                        "Title" :title.replace('\u2019', ''),
                        "author_name" :author.replace('\u00e9',''),
                        "price" :price,
                        "link": link
                    })
                
                
            load_more = browser.find_element(By.CSS_SELECTOR,'.loading-page')
            # time.sleep(1)
            load_more.click()
        else:
            load_more = False
            break

    except:
        load_more = False
    
    

with open('online_books_02.json','w') as j:
    json.dump(books_dic,j, indent = 4)


