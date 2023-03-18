from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import re
import mysql.connector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from multiprocessing import Process
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="products"
)

cursor=mydb.cursor()
def insertsql(v1,v2,v3,v4,v5):
    sql="INSERT INTO productstable2 (Product_name, Product_price, Product_link, Product_image, Product_site) VALUES (%s, %s, %s, %s, %s)"
    val=(v1,v2,v3,v4,v5)
    try:
        cursor.execute(sql, val)    
    except:
        sql2="UPDATE productstable2 SET Product_name=%s, Product_price=%s, Product_image=%s, Product_site=%s WHERE Product_link=%s"
        val2=(v1,v2,v4,v5,v3)
        cursor.execute(sql2, val2)
    mydb.commit()

b1="asdasdas"
b2=500
b3="sdfdsfsd"
b4="dsfsdfsdfsdf344"
b5="435gfhnbvnvb"

options = webdriver.ChromeOptions() 
#prefs = {"profile.managed_default_content_settings.images": 2}
#options.add_experimental_option("prefs", prefs)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
#options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--window-size=1920,1080')


driver=webdriver.Chrome('scripts/chromedriver.exe',options=options)

brands=["samsung", "apple", "xiaomi", "huawei", "oppo","lg","oneplus","jbl","sony","steelseries","sennheiser","msi","lenovo","razer","logitech","philips","monster","hp","asus","benq","casper",
"acer","aoc","dell","canon","anker","nikon","everest","gamepower","bosch","fakir","general mobile","htc","intel","microsoft","nokia","toshiba","kingston","hyperx","vestel","xp"]
products=[]
product_data=[]
list1=[]  
list2=[]
list3=[]

    


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

brands=["monitör"]
page1product1=""
def hepsiburada():
    for br in brands:
        x=0
        z=1
        while z==1:
            x+=1
            pd2=br.replace(" ","%20")
            link="https://www.hepsiburada.com/ara?q="+pd2+"&sayfa="+str(x)
            driver.get(link)
            while True:
                
                print("1")
                
                try:
                    
            
                    p_class= driver.find_elements(By.XPATH, '//li[@class="productListContent-zAP0Y5msy8OHn5z7T_K_"]')
                    
                    
                    break
                except:
                    time.sleep(5)
                    pass

            print("2")
            if x==1:
                page1product1=driver.find_element(By.XPATH,'//ul/li/div/a[@href]').get_attribute('href')                                                      
            for product in p_class:

                try:
                    print("2.5")
                    price= product.find_element(By.XPATH,'.//div[@data-test-id="price-current-price"]').text[:-3].replace(".","").replace(",",".")
                    
                    info= product.find_element(By.XPATH,'.//h3[@data-test-id="product-card-name"]').text.lower() 
                    pic= product.find_element(By.XPATH,'.//img[@class]')
                    picurl=pic.get_attribute('src')
                    url=product.find_element(By.XPATH,'.//a[@target="_blank"]')
                    link=url.get_attribute('href')  
                    print(link)
                    if x!=1 and link==page1product1:
                        z=0
                        print(page1product1)
                        break
                    
                    site="HepsiBurada"
                except:
                    continue
                insertsql(info,price,link,picurl,site)
            print("3")

def amazon():
    for br in brands:
        x=0
        
        while True:
            x+=1
            pd2=br.replace(" ","+")
            link="https://www.amazon.com.tr/s?k="+pd2+"&page="+str(x)
            driver.get(link)
            while True:
                try:

                    p_class=driver.find_elements(By.XPATH,'//div[@data-component-type="s-search-result"]')

                    break
                except:
                    pass
            print("2")

            for product in p_class:

                try:
                    print("2.5")
                    price= product.find_element(By.XPATH,'.//span[@class="a-price"]').text[:-2].replace('\n',',').replace(".","").replace(",",".")
                    print(price)
                    info= product.find_element(By.XPATH,'.//span[@class="a-size-base a-color-base a-text-normal"]').text.lower()
                    pic= product.find_element(By.XPATH,'.//div/div/div/div/div/span/a/div/img[@src]')
                    picurl=pic.get_attribute('src')
                    url=product.find_element(By.XPATH,'.//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
                    link= url.get_attribute('href')
                    

                    
                    
                except:
                    try:
                        price= product.find_element(By.XPATH,'.//span[@class="a-price"]').text[:-2].replace('\n',',').replace(".","").replace(",",".")
                        info= product.find_element(By.XPATH,'.//span[@class="a-size-base-plus a-color-base a-text-normal"]').text.lower()
                        pic= product.find_element(By.XPATH,'.//div/div/div/div/div/span/a/div/img[@src]')
                        picurl=pic.get_attribute('src')
                        url=product.find_element(By.XPATH,'.//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
                        link= url.get_attribute('href')
                        


                    except:
                        continue
                site="Amazon"
                print((info,price,link,picurl,site))
                insertsql(info,price,link,picurl,site)
            if len(p_class)==0:
                break
                

def trendyol():
    driver2=webdriver.Chrome('scripts/chromedriver2.exe',options=options)
    print("trendyol basladiiiiiiiiii")
    for br in brands:
        x=0

        while True:
            x+=1
            pd2=br.replace(" ","%20")
            link="https://www.trendyol.com/sr?q="+pd2+"&pi="+str(x)
            driver2.get(link)
            driver2.execute_script("document.body.style.zoom='25%'")
            while True:
                


                try:
                    
                    
                    p_class= driver2.find_elements(By.XPATH,'//div[@class="prdct-cntnr-wrppr"]/div')
                    
                    
                    break
                except:
                    pass


    
            for z,product in enumerate(p_class):
    
                try:

                    price= product.find_element(By.XPATH,'.//div[@class="prc-box-dscntd"]').text[:-3].replace('\n',',').replace(".","").replace(",",".")

                    info2=  product.find_elements(By.XPATH,'.//div[@class="prdct-desc-cntnr-ttl-w two-line-text"]/span') 
                    info=""
                    for i in info2:
                        try:
                            if i==info2[0]:
                                info=i.text.lower()+" "
                            elif i==info2[1]:
                                info=info+i.text.lower()
                        except:
                            pass

                    pic= product.find_element(By.XPATH,'.//img')
                
                    picurl=pic.get_attribute('src')
                    print(picurl)
                    url=product.find_element(By.XPATH,'.//div/a[@href]')

                    link=url.get_attribute('href')
                    print(link)

                    
                    site="Trendyol"
                except:
                    continue
                insertsql(info,price,link,picurl,site)


def ciceksepeti():
    for br in brands:
        x=0
        z=1
        while z==1:
            x+=1
            pd2=br.replace(" ","%20")
            "https://www.ciceksepeti.com/arama?query=iphone%2014&qt=iphone%2014&choice=2"
            link="https://www.ciceksepeti.com/arama?query="+pd2+"&page="+str(x)
            driver.get(link)
            while True:
                
                print("1")
                
                try:
                    
                    
                    p_class= driver.find_elements(By.XPATH, '//div[@class="products products--category js-ajax-category-products"]/div')
                    print("1,5")
                    
                    break
                except:
                    pass
            if driver.current_url=="https://www.ciceksepeti.com/arama?query="+pd2:
                break
            print("2")                                               
            for product in p_class:

                try:
                    print("2.5")
                    price= product.find_element(By.XPATH,'.//div[@class="price price--now"]/div[@class="price__left"]/span[@class="price__integer-value"]').text.replace(".","")
                    
                    info= product.find_element(By.XPATH,'.//p[@class="products__item-title"]').text.lower() 
                    pic= product.find_element(By.XPATH,'.//img')
                    picurl=pic.get_attribute('data-src')
                    url=product.find_element(By.XPATH,'.//a[@class="products__item-link js-products__item-link"]')
                    link=url.get_attribute('href')  
                    print(link)

                    
                    site="CicekSepeti"
                except:
                    continue
                insertsql(info,price,link,picurl,site)
            print("3")


if __name__ == '__main__':
    p1 = Process(target=hepsiburada())
    p2 = Process(target=trendyol())
    p1.start()
    p2.start()
