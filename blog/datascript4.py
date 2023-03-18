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
from blog.models import Products
"""
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
"""
b1="asdasdas"
b2=500
b3="sdfdsfsd"
b4="dsfsdfsdfsdf344"
b5="435gfhnbvnvb"

options = webdriver.ChromeOptions() 
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--window-size=1920,1080')

driver=webdriver.Chrome('chromedriver',options=options)

brands=["samsung", "apple", "xiaomi", "huawei", "oppo","lg","oneplus","jbl","sony","steelseries","sennheiser","msi","lenovo","razer","logitech","philips","monster","hp","asus","benq","casper",
"acer","aoc","dell","canon","anker","nikon","everest","gamepower","bosch","fakir","general mobile","htc","intel","microsoft","nokia","toshiba","kingston","hyperx","vestel","xp"]
products=[]
product_data=[]
list1=[]  
list2=[]
list3=[]

    


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


page1product1=""

brands = ["Monitör"]
for br in brands:
    x=0
    z=1
    while z==1:
        x+=1
        pd2=br.replace(" ","%20")
        "https://www.ciceksepeti.com/arama?query=iphone%2014&qt=iphone%2014&choice=2"
        link="https://www.ciceksepeti.com/arama?query="+pd2+"&page="+str(x)
        driver.get(link)
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(0,document.documentBody)")
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(0,document.documentBody)")
        
        while True:
            
            print("1")
            
            try:
                
                
                p_class= driver.find_elements(By.XPATH, '//div[@class="products products--category js-ajax-category-products"]/div')[0:70]
                print("1,5")
                
                break
            except:
                pass
        if driver.current_url=="https://www.ciceksepeti.com/arama?query="+pd2:
            break
        print("2")     
        i=0                                          
        for product in p_class:
            i+=1
            try:
                print(i)
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
            product = Products(Product_name=info,Product_price=price,Product_link=link,Product_image=picurl,Product_site=site) # create new model instance
            
            Products.objects.update_or_create(Product_name=info,Product_price=price,Product_link=link,Product_image=picurl,Product_site=site) 
        print("3")


