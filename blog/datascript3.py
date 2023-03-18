from selenium import webdriver
import time
from selenium.webdriver.common.by import By
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


options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
#options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--no-sandbox")
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
for br in brands:
    x=0

    while True:
        x+=1
        pd2=br.replace(" ","%20")
        link="https://www.trendyol.com/sr?q="+pd2+"&pi="+str(x)
        driver.get(link)
        driver.execute_script("document.body.style.zoom='25%'")
        time.sleep(1.5)
        p_class= driver.find_elements(By.XPATH,'//div[@class="prdct-cntnr-wrppr"]/div')



 
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
            #product = Products(Product_name=info,Product_price=price,Product_image=picurl,Product_site=site,) # create new model instance
            
            Products.objects.update_or_create(Product_link=link,defaults={"Product_name":info,"Product_price":price,"Product_link":link,"Product_image":picurl,"Product_site":site}) 



