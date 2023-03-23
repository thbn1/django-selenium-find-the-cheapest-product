from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
import re
import mysql.connector

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
#prefs = {"profile.managed_default_content_settings.images": 2}
#options.add_experimental_option("prefs", prefs)
#options.add_experimental_option("excludeSwitches", ["enable-logging"])

#options.add_argument("--disable-gpu")
#options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
#options.add_argument("--no-sandbox")
#options.add_argument("--disable-dev-shm-usage")
options.add_argument('--window-size=1920,1080')

driver=webdriver.Chrome(options=options)
driver.execute_script("document.body.style.zoom='50%'")

brands=["samsung", "apple", "xiaomi", "huawei", "oppo","lg","oneplus","jbl","sony","steelseries","sennheiser","msi","lenovo","razer","logitech","philips","monster","hp","asus","benq","casper",
"acer","aoc","dell","canon","anker","nikon","everest","gamepower","bosch","fakir","general mobile","htc","intel","microsoft","nokia","toshiba","kingston","hyperx","vestel"]
brands=["samsung","apple", "xiaomi", "huawei", "oppo","lg","msi","lenovo","razer","logitech","philips","monster","acer","aoc","dell","asus"]

products=[]
product_data=[]
list1=[]  
list2=[]
list3=[]

    
firstelement=""

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

page1product1=""
for br in brands:
    x=0
    z=1
    y=0
    while z==1:
        x+=1
        pd2=br.replace(" ","%20")
        link="https://www.hepsiburada.com/ara?q="+pd2+'&markalar='+pd2.lower()+"&sayfa="+str(x)+"&ic=t"
        #link="https://www.hepsiburada.com/ara?q=galaxy%20a04e'&markalar=Samsung&sayfa="+str(x)
        "https://www.hepsiburada.com/ara?q=Samsung&markalar=samsung"
     
        driver.get(link)
        time.sleep(0.3)
        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(0.1)
        driver.execute_script("window.scrollTo(500,1000)")
        time.sleep(0.1)
        driver.execute_script("window.scrollTo(1000,1500)")
        time.sleep(0.1)
        driver.execute_script("window.scrollTo(1500,2000)")
        time.sleep(0.1)
        driver.execute_script("window.scrollTo(2000,2500)")
        time.sleep(0.1)

        print("1")
            
        
        try:
            p_class= driver.find_elements(By.XPATH, '//li[@class="productListContent-zAP0Y5msy8OHn5z7T_K_"]')[0:24]
        except:break

        if len(p_class)==0:
            break
        if firstelement == p_class[0].find_element(By.XPATH,'.//a[contains(@class,"moria-ProductCard")]').get_attribute('href'):
            y+=1
        if y==3:
            break
        
        
        firstelement=p_class[0].find_element(By.XPATH,'.//a[contains(@class,"moria-ProductCard")]').get_attribute('href')

            
        l=0                                                  
        for product in p_class:
            print("---------------")
            l+=1
            try:
                
                price= product.find_element(By.XPATH,'.//div[@data-test-id="price-current-price"]').text[:-3].replace(".","").replace(",",".")
                
                info= product.find_element(By.XPATH,'.//h3[@data-test-id="product-card-name"]').text.lower() 
                pic= product.find_element(By.XPATH,'.//div[@data-test-id="product-image-image"]/picture/img')
                picurl=pic.get_attribute('src')
                url=product.find_element(By.XPATH,'.//a[contains(@class,"moria-ProductCard")]')
                link=url.get_attribute('href')  
                "https%3A%2F%2Fwww.hepsiburada.com%2Fsamsung-galaxy-a04e-128-gb-4-gb-ram-samsung-turkiye-garantili-p-HBCV00003LC1OV%3Fmagaza%3DHepsiburada&eventName=sp-click&platform=desktop"
                if "https://adservice.hepsiburada.com" in link:
                    link=link.split("redirect=")[-1].replace("%2F","/").replace("%3A",":").replace("%3F","?").replace("%3D","=")
                site="HepsiBurada"
                print(picurl)
                print(link)
                print(l)
                if l==24:
                   
                    print("breaK")
                    break
            except:continue #
            #product = Products(Product_name=info,Product_price=price,Product_link=link,Product_image=picurl,Product_site=site) # create new model instance
            
                        #product = Products(Product_name=info,Product_price=price,Product_link=link,Product_image=picurl,Product_site=site) # create new model instance
            Products.objects.update_or_create(Product_link=link,defaults={"Product_name":info,"Product_price":price,"Product_link":link,"Product_image":picurl,"Product_site":site}) 
            print("basarili")
            
        print("3")
        print("3")




